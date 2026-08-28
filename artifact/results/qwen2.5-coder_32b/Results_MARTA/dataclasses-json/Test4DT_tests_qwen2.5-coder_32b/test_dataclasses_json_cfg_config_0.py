
import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError

def test_config_with_custom_encoder_and_decoder():
    def custom_encoder(obj):
        return str(obj)

    def custom_decoder(data):
        return int(data)

    metadata = config(encoder=custom_encoder, decoder=custom_decoder)
    assert metadata['dataclasses_json']['encoder'] == custom_encoder
    assert metadata['dataclasses_json']['decoder'] == custom_decoder

def test_config_with_letter_case():
    from dataclasses_json import LetterCase

    metadata = config(letter_case=LetterCase.CAMEL)
    assert metadata['dataclasses_json']['letter_case'] == LetterCase.CAMEL


def test_config_with_field_name_and_letter_case():
    from dataclasses_json import LetterCase

    def letter_case_func(name):
        return name.upper()

    metadata = config(letter_case=letter_case_func, field_name='user_id')
    assert callable(metadata['dataclasses_json']['letter_case'])
    assert metadata['dataclasses_json']['letter_case']('user_id') == 'USER_ID'

def test_config_with_marshmallow_field():
    from marshmallow.fields import Integer as MarshmallowField

    metadata = config(mm_field=MarshmallowField)
    assert metadata['dataclasses_json']['mm_field'] == MarshmallowField

def test_config_with_exclude_function():
    def exclude_fields(name, value):
        return name.startswith('temp_')

    metadata = config(exclude=exclude_fields)
    assert metadata['dataclasses_json']['exclude'] == exclude_fields

def test_config_with_existing_metadata():
    existing_metadata = {'dataclasses_json': {'encoder': str}}

    metadata = config(metadata=existing_metadata, decoder=int)
    assert metadata['dataclasses_json']['encoder'] == str
    assert metadata['dataclasses_json']['decoder'] == int