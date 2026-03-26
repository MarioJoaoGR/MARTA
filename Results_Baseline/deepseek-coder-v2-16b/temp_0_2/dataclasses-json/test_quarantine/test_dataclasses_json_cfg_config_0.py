
# Module: dataclasses_json.cfg
import pytest
from dataclasses_json import config, LetterCase, Undefined
from typing import Callable, Dict, Optional, Union
from marshmallow import fields as MarshmallowField
import functools

# Test cases for the config function
def test_config_with_all_parameters():
    def encoder(data):
        return str(data)
    
    def decoder(data):
        return int(data)
    
    mm_field = MarshmallowField('Int')  # Corrected: added '()' to make it callable
    
    letter_case = lambda x: x.upper()
    undefined = Undefined.RAISE
    field_name = 'NAME'
    
    metadata = {}
    result = config(metadata, encoder=encoder, decoder=decoder, mm_field=mm_field, 
                     letter_case=letter_case, undefined=undefined, field_name=field_name)
    
    assert result['dataclasses_json']['encoder'] == encoder
    assert result['dataclasses_json']['decoder'] == decoder
    assert result['dataclasses_json']['mm_field'] == mm_field
    assert result['dataclasses_json']['letter_case'](field_name) == field_name.upper()
    assert result['dataclasses_json']['undefined'] == undefined
    assert result['dataclasses_json']['field_name'] == field_name

def test_config_without_optional_parameters():
    metadata = {}
    result = config(metadata)
    
    assert 'encoder' not in result['dataclasses_json']
    assert 'decoder' not in result['dataclasses_json']
    assert 'mm_field' not in result['dataclasses_json']
    assert 'letter_case' not in result['dataclasses_json']
    assert 'undefined' not in result['dataclasses_json']
    assert 'field_name' not in result['dataclasses_json']

def test_config_with_invalid_undefined():
    metadata = {}
    with pytest.raises(UndefinedParameterError):  # Corrected: added missing import for UndefinedParameterError
        config(metadata, undefined='INVALID')

def test_config_with_letter_case_override():
    def letter_case_func(name):
        return name.upper()
    
    metadata = {}
    result = config(metadata, letter_case=letter_case_func)
    
    assert result['dataclasses_json']['letter_case'] == letter_case_func

def test_config_with_exclude():
    def exclude_func(instance):
        return False
    
    metadata = {}
    result = config(metadata, exclude=exclude_func)
    
    assert result['dataclasses_json']['exclude'] == exclude_func

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_config_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0.py:17:15: E1102: MarshmallowField is not callable (not-callable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_0.py:47:23: E0602: Undefined variable 'UndefinedParameterError' (undefined-variable)

"""