
import pytest
from dataclasses_json.undefined import _IgnoreUndefinedParameters
from typing import Dict, Any

# Test Scenario 1: test_undefined_parameters
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py F [100%]

=================================== FAILURES ===================================
__________________________ test_undefined_parameters ___________________________

    def test_undefined_parameters():
        kvs = {'param1': 1}
        with pytest.raises(TypeError):
>           known_params = _IgnoreUndefinedParameters.handle_from_dict(MyClass, kvs)
E           NameError: name 'MyClass' is not defined

/opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py:10: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/dataclasses-json/Test4DT_tests_deepseek-coder-v2_16b/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_0.py::test_undefined_parameters
============================== 1 failed in 0.07s ===============================
"""