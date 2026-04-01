
import pytest
from dataclasses import dataclass
from typing import Optional, Callable, Dict, Union, List
from dataclasses_json import dataclass_json, config
from marshmallow import fields as MarshmallowField
from enum import Enum

class LetterCase(Enum):
    LOWER = 'lower'
    UPPER = 'upper'
    CAMEL = 'camel'

class Undefined(Enum):
    IGNORE = 'ignore'
    EXCLUDE = 'exclude'

@dataclass_json
@dataclass
class Example:
    name: str
    age: int

def test_config():
    metadata = {}
    encoder = lambda x: x
    decoder = lambda y: y
    mm_field = MarshmallowField()
    letter_case = LetterCase.LOWER
    undefined = Undefined.EXCLUDE
    field_name = 'name'
    exclude = lambda instance: False

    result = config(metadata, encoder=encoder, decoder=decoder, mm_field=mm_field, letter_case=letter_case, undefined=undefined, field_name=field_name, exclude=exclude)

    assert 'dataclasses_json' in result[metadata]
    assert result['dataclasses_json']['encoder'] == encoder
    assert result['dataclasses_json']['decoder'] == decoder
    assert result['dataclasses_json']['mm_field'] == mm_field
    assert result['dataclasses_json']['letter_case'](field_name) == field_name.lower()
    assert result['dataclasses_json']['undefined'] == undefined
    assert result['dataclasses_json']['exclude'] == exclude

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_config_0_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0_test_edge_cases.py:28:15: E1102: MarshmallowField is not callable (not-callable)


"""