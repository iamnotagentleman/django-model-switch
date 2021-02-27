from core.main import BaseGenerator
from enums.main import PonyParamEnum, PonyTypeEnumIn, PonyTypeEnumSub
import logging


class PonyOrmGenerator(BaseGenerator):
    @staticmethod
    def get_prefix(field):
        try:
            relation_ship = field.relationship
            return PonyTypeEnumSub.foreign_key.value
        except KeyError:
            return PonyParamEnum.required.value if field.params.get('required') else PonyParamEnum.optional.value

    @staticmethod
    def get_in_type(field):
        try:
            return f"'{field.relationship}'"
        except KeyError:
            return PonyTypeEnumIn.get(field.type)

    @classmethod
    def generate_pony_fields_from_list(cls, data):
        suffix = ')'
        for field in data:
            model_field = f"{field.name} = {cls.get_prefix(field=field)}({cls.get_in_type(field)}"
            for param in field.params:
                enumed = PonyParamEnum.get(param)
                if enumed:
                    model_field += f", {enumed}={field.params[param]}"
                else:
                    logging.warning(f'{param} not found in {PonyParamEnum.keys()}')
            yield model_field + suffix
