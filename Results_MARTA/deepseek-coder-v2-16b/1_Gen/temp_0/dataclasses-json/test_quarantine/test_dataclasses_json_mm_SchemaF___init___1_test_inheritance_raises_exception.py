
import pytest
from dataclasses_json.mm import SchemaF

def test_inheritance_raises_exception():
    with pytest.raises(NotImplementedError):
        class InheritedSchemaF(SchemaF):
            pass

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF___init___1_test_inheritance_raises_exception.py F [100%]

=================================== FAILURES ===================================
______________________ test_inheritance_raises_exception _______________________

    def test_inheritance_raises_exception():
>       with pytest.raises(NotImplementedError):
E       Failed: DID NOT RAISE <class 'NotImplementedError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF___init___1_test_inheritance_raises_exception.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_SchemaF___init___1_test_inheritance_raises_exception.py::test_inheritance_raises_exception
============================== 1 failed in 0.03s ===============================

"""