
from dataclasses import dataclass, fields
from typing import Type, Dict, Any
from dataclasses_json.core import _decode_dataclass
from dataclasses_json.core import is_dataclass, get_type_hints
from dataclasses_json.core import _isinstance_safe, _user_overrides_or_exts, _handle_undefined_parameters_safe
from dataclasses_json.core import _decode_letter_case_overrides, _decode_generic, _support_extended_types
from dataclasses_json.core import _is_optional, _is_new_type, _is_supported_generic
import warnings

@dataclass
class Person:
    name: str
    age: int = 0

def test_valid_case():
    from dataclasses_json import dataclass_json
    
    @dataclass_json
    @dataclass
    class Person:
        name: str
        age: int = 0

    # Create a Person instance from JSON string
    person = Person.from_dict({"name": "John Doe", "age": 30})
    assert person == Person(name='John Doe', age=30)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_core__decode_dataclass_1_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_1_test_valid_case.py:26:13: E1101: Class 'Person' has no 'from_dict' member (no-member)


"""