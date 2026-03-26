
import pytest
from dataclasses import dataclass
from typing import Optional, Callable, Dict, Union
from marshmallow import fields as MarshmallowField
from dataclasses_json.cfg import config
from dataclasses_json import Undefined, LetterCase

def test_config():
    @dataclass
    class Example:
        a: int
        b: str = "default"
        c: Optional[int] = None

    metadata = {}
    new_metadata = config(metadata, encoder=lambda x: x, decoder=lambda y: y)
    
    assert 'dataclasses_json' in new_metadata
    assert 'encoder' in new_metadata['dataclasses_json']
    assert callable(new_metadata['dataclasses_json']['encoder'])
    assert 'decoder' in new_metadata['dataclasses_json']
    assert callable(new_metadata['dataclasses_json']['decoder'])

    # Test letter case conversion
    @config(letter_case=lambda s: s.upper())
    @dataclass
    class Example2:
        a_camel_case: int

    example = Example2(a_camel_case=1)
    assert example.to_dict() == {'A_CAMEL_CASE': 1}

    # Test handling undefined parameters
    @dataclass
    class Example3:
        a: int
        b: str = "default"

    metadata = {}
    new_metadata = config(metadata, undefined="ignore")
    
    assert 'undefined' in new_metadata['dataclasses_json']
    assert new_metadata['dataclasses_json']['undefined'] == Undefined.IGNORE

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg_config_3_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_3_test_invalid_inputs.py:32:11: E1101: Instance of 'Example2' has no 'to_dict' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg_config_3_test_invalid_inputs.py:44:60: E1101: Class 'Undefined' has no 'IGNORE' member (no-member)


"""