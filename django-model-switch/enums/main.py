from enum import Enum
__all__  = ['PonyParamEnum',
            'PonyTypeEnumIn',
            'PonyTypeEnumSub',
            'FieldTypeEnum',
            'TargetEnum',
            'OutEnum',
            'ModelEnum']

PONY_EXCLUDED_ARGS = ('verbose_name',
                      'editable',
                      'verbose_name',
                      'spatial_index',
                      )


class CoreEnum(Enum):

    @classmethod
    def get(cls, key):
        try:
            key = cls[key].value
            return key
        except KeyError:
            return None

    @classmethod
    def keys(cls):
        return [i for i in cls.__dict__.keys() if i[:1] != '_']

class PonyTypeEnumIn(CoreEnum):
    string = "str"
    unsigned_int = "int"
    date = "datetime"
    boolean = "bool"


class PonyTypeEnumSub(CoreEnum):
    foreign_key = "Set"
    many_to_many = "Set"


class PonyParamEnum(CoreEnum):
    required = "Required"
    optional = "Optional"
    max_length = "max_len"
    primary_key = "PrimaryKey"
    null = "nullable"
    unique = "unique"
    boolean = "bool"
    default = "default"


class FieldTypeEnum(CoreEnum):
    CharField = "string"
    IntegerField = "int"
    EmailField = "string"
    BooleanField = "boolean"
    DateTimeField = "date"
    DateField = "date",
    TimeField = "time",
    FileField = "string",
    ForeignKey = "foreign_key"
    ManyToManyField = "many_to_many"
    OneToOneField = "foreign_key"
    PositiveIntegerField = "unsigned_int"


class ModelEnum(CoreEnum):
    MODEL_BASE_CLASSES = ["CoreModel", "Model", 'models.Model']
    DEFAULT_FIELD_TYPE = "string"


class TargetEnum(CoreEnum):
    PYDANTIC = "pydantic"
    PONY = "pony"
    TORTOISE = "tortoise"


class OutEnum(CoreEnum):
    default = "stdout"
