from enum import Enum


class CoreEnum(Enum):

    @classmethod
    def get(cls, key):
        try:
            key = cls[key].value
            return key
        except KeyError:
            return None

    @classmethod
    def keys(self):
        return [i for i in self.__dict__.keys() if i[:1] != '_']

class PonyTypeEnumIn(CoreEnum):
    string = "str"
    unsigned_int = "int"
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
    DateTimeField = "datetime"
    DateField = "date",
    TimeField = "time",
    FileField = "string",
    ForeignKey = "foreign_key"
    ManyToManyField = "many_to_many"
    OneToOneField = "foreign_key"
    PositiveIntegerField = "unsigned_int"


class ModelEnum(CoreEnum):
    MODEL_BASE_CLASSES = ["CoreModel", "Model"]
    DEFAULT_FIELD_TYPE = "string"


class TargetEnum(CoreEnum):
    PYDANTIC = "pydantic"
    PONY = "pony"
    TORTOISE = "tortoise"


class OutEnum(CoreEnum):
    default = "stdout"
