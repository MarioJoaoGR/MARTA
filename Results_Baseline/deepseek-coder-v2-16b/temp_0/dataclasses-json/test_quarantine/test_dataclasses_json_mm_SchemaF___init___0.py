
# Module: dataclasses_json.mm
# test_schemaf.py
from your_module import SchemaF
import pytest

def test_schemaf_instantiation():
    with pytest.raises(NotImplementedError):
        SchemaF()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_SchemaF___init___0
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF___init___0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""