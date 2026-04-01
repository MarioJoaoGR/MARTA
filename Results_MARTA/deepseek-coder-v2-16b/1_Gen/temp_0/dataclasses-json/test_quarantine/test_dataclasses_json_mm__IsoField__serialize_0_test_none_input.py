
from dataclasses import dataclass, field
from datetime import datetime
import pytest
from dataclasses_json.mm import ValidationError
from .test_dataclasses_json_mm__IsoField__serialize_0_test_none_input import _IsoField, MyModel

@pytest.fixture
def setup_model():
    class MyModel:
        field = _IsoField()
    
    return MyModel()

def test_none_input(setup_model):
    model_instance = setup_model
    with pytest.raises(ValidationError) as excinfo:
        model_instance._serialize(None, "field", model_instance)
    assert str(excinfo.value) == '_IsoField().default_error_messages["required"]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_none_input.py _
ImportError while importing test module '/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_none_input.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/homebrew/Caskroom/miniconda/base/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_none_input.py:6: in <module>
    from .test_dataclasses_json_mm__IsoField__serialize_0_test_none_input import _IsoField, MyModel
E   ImportError: cannot import name '_IsoField' from partially initialized module 'Test4DT_tests.test_dataclasses_json_mm__IsoField__serialize_0_test_none_input' (most likely due to a circular import) (/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_none_input.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_0_test_none_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.06s ===============================

"""