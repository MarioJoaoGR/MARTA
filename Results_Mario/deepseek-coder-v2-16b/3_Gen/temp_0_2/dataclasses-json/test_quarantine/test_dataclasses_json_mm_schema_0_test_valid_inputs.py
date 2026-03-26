
import pytest
from dataclasses import dataclass, fields as dc_fields
from typing import Optional, List, Union
from marshmallow import Schema, fields
from dataclasses_json.mm import schema as dc_schema

@dataclass
class MyDataClass:
    name: str
    age: int = 30
    active: bool = True

class MyMixin: pass

def test_valid_inputs():
    # Define expected schema based on MyDataClass
    expected_schema = {
        'name': fields.Str(),
        'age': fields.Int(default=30),
        'active': fields.Bool(default=True)
    }
    
    # Generate the schema using the function under test
    generated_schema = dc_schema(MyDataClass, MyMixin, infer_missing=True)
    
    # Assert that the generated schema matches the expected schema
    assert generated_schema == expected_schema

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Define expected schema based on MyDataClass
        expected_schema = {
            'name': fields.Str(),
            'age': fields.Int(default=30),
            'active': fields.Bool(default=True)
        }
    
        # Generate the schema using the function under test
        generated_schema = dc_schema(MyDataClass, MyMixin, infer_missing=True)
    
        # Assert that the generated schema matches the expected schema
>       assert generated_schema == expected_schema
E       AssertionError: assert {'active': <f...8 string.'})>} == {'active': <f...8 string.'})>}
E         
E         Differing items:
E         {'name': <fields.String(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=True, load_only=Fa...'validator_failed': 'Invalid value.', 'invalid': 'Not a valid string.', 'invalid_utf8': 'Not a valid utf-8 string.'})>} != {'name': <fields.String(dump_default=<marshmallow.missing>, attribute=None, validate=None, required=False, load_only=F...'validator_failed': 'Invalid value.', 'invalid': 'Not a valid string.', 'invalid_utf8': 'Not a valid utf-8 string.'})>}
E         {'age': <fields.Integer(dump_default=<marshmallow.missing>, attribute=None, ...
E         
E         ...Full output truncated (3 lines hidden), use '-vv' to show

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py:28: AssertionError
=============================== warnings summary ===============================
Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py::test_valid_inputs
  /opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/site-packages/marshmallow/fields.py:986: RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.
    super().__init__(**kwargs)

Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py::test_valid_inputs
  /opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/site-packages/marshmallow/fields.py:1218: RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.
    super().__init__(**kwargs)

Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py::test_valid_inputs
  /opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/site-packages/marshmallow/fields.py:986: RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.
    super().__init__(**kwargs)

Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py::test_valid_inputs
  /opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/site-packages/marshmallow/fields.py:1218: RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.
    super().__init__(**kwargs)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_schema_0_test_valid_inputs.py::test_valid_inputs
======================== 1 failed, 4 warnings in 0.03s =========================
"""