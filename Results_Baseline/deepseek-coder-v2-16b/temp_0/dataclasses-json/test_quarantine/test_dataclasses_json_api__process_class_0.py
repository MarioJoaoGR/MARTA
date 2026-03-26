
# Module: dataclasses_json.api
# test_dataclasses_json.py
from dataclasses import dataclass
from typing import Optional, Union
from dataclasses_json import dataclass_json, LetterCase, config, Undefined
import pytest

@pytest.fixture
def example_class():
    @dataclass_json
    @dataclass
    class Example:
        a: int
        b: str = "default"
        c: Optional[int] = None
    
    def _process_class(cls, letter_case=None, undefined=Undefined.EXCLUDE):
        if letter_case:
            cls = dataclass_json(letter_case=letter_case)(cls)
        if undefined:
            cls = dataclass_json(undefined=undefined)(cls)
        return cls
    
    return _process_class(Example, LetterCase.CAMEL, Undefined.EXCLUDE)

def test_example_class_with_defaults(example_class):
    example = example_class(a=1, b="test", c=None)
    assert example.to_dict() == {'a': 1, 'b': 'default', 'c': None}
    assert example.to_json() == '{"a": 1, "b": "default", "c": null}'

def test_example_class_with_custom_config(example_class):
    @config(letter_case=lambda s: s.upper())
    @dataclass_json
    @dataclass
    class Example2:
        a_camel_case: int
    
    example2 = _process_class(Example2, None, Undefined.EXCLUDE)(a_camel_case=1)
    assert example2.to_dict() == {'A_CAMEL_CASE': 1}
    assert example2.to_json() == '{"A_CAMEL_CASE": 1}'

def test_example_class_with_undefined(example_class):
    @dataclass_json
    @dataclass
    class Example3:
        a: int
        b: str = "default"
    
    example3 = _process_class(Example3, LetterCase.CAMEL, Undefined.EXCLUDE)(a=1)
    assert example3.to_dict() == {'a': 1}
    assert example3.to_json() == '{"a": 1}'

def test_example_class_with_all_params(example_class):
    @config(letter_case=LetterCase.CAMEL, undefined=Undefined.EXCLUDE)
    @dataclass_json
    @dataclass
    class Example4:
        a: int
        b: str = "default"
        c: Optional[int] = None
    
    example4 = Example4(a=1, b="test", c=None)
    assert example4.to_dict() == {'a': 1, 'b': 'test', 'c': None}
    assert example4.to_json() == '{"a": 1, "b": "test", "c": null}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api__process_class_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_api__process_class_0.py:39:15: E0602: Undefined variable '_process_class' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api__process_class_0.py:50:15: E0602: Undefined variable '_process_class' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api__process_class_0.py:64:11: E1101: Instance of 'Example4' has no 'to_dict' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api__process_class_0.py:65:11: E1101: Instance of 'Example4' has no 'to_json' member (no-member)

"""