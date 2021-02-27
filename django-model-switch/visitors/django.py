import ast
from _ast import Call, Attribute, Name

from enums.main import FieldTypeEnum, ModelEnum
from utils import AttrDict


class FieldVisitor(ast.NodeVisitor):
    """
    A visitor that inspects model fields.
    """
    def __init__(self):
        self.fields = []

    def add_field(self, field_name, field_type, relationship, params):
        field = AttrDict()
        field.name = field_name
        field.type = field_type
        field.params = params
        if relationship is not None:
            field.relationship = relationship
        self.fields.append(field)

    def visit_Assign(self, node):
        field_name = None
        field_type = None
        relationship = None
        params = AttrDict()

        if not isinstance(node.value, Call):
            return

        field_name = node.targets[0].id
        if isinstance(node.value.func, Attribute):
            field_type = FieldTypeEnum.get(node.value.func.attr) if FieldTypeEnum.get(node.value.func.attr) else ModelEnum.DEFAULT_FIELD_TYPE.value
            for i in node.value.keywords:
                if not isinstance(i.value, Call):
                    params[i.arg] = i.value.value
        if field_type in [FieldTypeEnum.ManyToManyField.value, FieldTypeEnum.ForeignKey.value]:
            relationship = node.value.args[0].value
        if field_type is not None:
            self.add_field(field_name, field_type, relationship=relationship, params=params)


class ModelVisitor(ast.NodeVisitor):
    """
    A visitor that detects django models.
    """
    def __init__(self):
        self.models = {}

    def visit_ClassDef(self, node):
        base_class = None
        for base in node.bases:
            if isinstance(base, Attribute):
                base_class = base.attr
            if isinstance(base, Name):
                base_class = base.id

        if base_class in ModelEnum.MODEL_BASE_CLASSES.value:
            visitor = FieldVisitor()
            visitor.visit(node)
            self.models[f'{node.name}({base_class})'] = visitor.fields