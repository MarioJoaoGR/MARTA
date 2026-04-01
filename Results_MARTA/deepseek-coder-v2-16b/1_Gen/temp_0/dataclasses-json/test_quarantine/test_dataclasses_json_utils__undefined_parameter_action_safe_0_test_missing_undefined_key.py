
import pytest
from dataclasses import dataclass, fields
from dataclasses_json import dataclass_json
from dataclasses_json.utils import _undefined_parameter_action_safe

@dataclass
class MyDataClass:
    dataclass_json_config = {'undefined': 'ignore'}

def test_missing_undefined_key():
    # Test when the class does not have a dataclass_json_config attribute
    @dataclass
    class NoConfigClass:
        pass
    
    assert _undefined_parameter_action_safe(NoConfigClass) is None

def test_with_valid_config():
    # Test when the config has an 'undefined' key with a valid value
    result = _undefined_parameter_action_safe(MyDataClass)
    assert result == 'ignore'

def test_invalid_config():
    # Test when the config has an 'undefined' key with an invalid value (None)
    @dataclass
    class InvalidConfigClass:
        dataclass_json_config = {'undefined': None}
    
    assert _undefined_parameter_action_safe(InvalidConfigClass) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__undefined_parameter_action_safe_0_test_missing_undefined_key.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_with_valid_config ____________________________

    def test_with_valid_config():
        # Test when the config has an 'undefined' key with a valid value
>       result = _undefined_parameter_action_safe(MyDataClass)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__undefined_parameter_action_safe_0_test_missing_undefined_key.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'Test4DT_tests.test_dataclasses_json_utils__undefined_parameter_action_safe_0_test_missing_undefined_key.MyDataClass'>

    def _undefined_parameter_action_safe(cls):
        try:
            if cls.dataclass_json_config is None:
                return
            action_enum = cls.dataclass_json_config['undefined']
        except (AttributeError, KeyError):
            return
    
>       if action_enum is None or action_enum.value is None:
E       AttributeError: 'str' object has no attribute 'value'

dataclasses-json/dataclasses_json/utils.py:186: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__undefined_parameter_action_safe_0_test_missing_undefined_key.py::test_with_valid_config
========================= 1 failed, 2 passed in 0.04s ==========================

"""