
from dataclasses import dataclass
import pytest
from dataclasses_json.utils import _undefined_parameter_action_safe

@dataclass
class MyDataClass:
    dataclass_json_config = {'undefined': 'some_value'}

def test_valid_input():
    assert _undefined_parameter_action_safe(MyDataClass) == 'some_value'

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__undefined_parameter_action_safe_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       assert _undefined_parameter_action_safe(MyDataClass) == 'some_value'

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__undefined_parameter_action_safe_1_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'Test4DT_tests.test_dataclasses_json_utils__undefined_parameter_action_safe_1_test_valid_input.MyDataClass'>

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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__undefined_parameter_action_safe_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""