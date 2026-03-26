
from dataclasses import dataclass
import pytest
from dataclasses_json.mm import Schema
from dataclasses_json import _ExtendedEncoder

@dataclass
class Person:
    name: str
    age: int

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))

    def to_json(self):
        return json.dumps(self, cls=json.JSONEncoder)

class CustomEncoder(json.JSONEncoder):
    pass

def test_valid_input_with_custom_encoder():
    person = Person(name="John Doe", age=30)
    json_string = person.to_json()
    assert json_string == '{"name": "John Doe", "age": 30}'

    # Test with custom encoder
    custom_json_string = person.to_json(cls=CustomEncoder)
    assert custom_json_string == '{"name": "John Doe", "age": 30}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder.py:5:0: E0611: No name '_ExtendedEncoder' in module 'dataclasses_json' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder.py:14:21: E0602: Undefined variable 'json' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder.py:17:15: E0602: Undefined variable 'json' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder.py:17:36: E0602: Undefined variable 'json' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder.py:19:20: E0602: Undefined variable 'json' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_dumps_5_test_valid_input_with_custom_encoder.py:28:25: E1123: Unexpected keyword argument 'cls' in method call (unexpected-keyword-arg)


"""