
import pytest
from dataclasses_json.core import _get_encoder_in_global_config
from unittest.mock import patch

# Mocking the cfg module and its global_config with encoders dictionary
@patch('dataclasses_json.core.cfg')
def test_none_input(_):
    # Test when type is None
    with pytest.raises(KeyError):
        _get_encoder_in_global_config(None)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

_ = <MagicMock name='cfg' id='4323047360'>

    @patch('dataclasses_json.core.cfg')
    def test_none_input(_):
        # Test when type is None
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input.py:10: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_core__get_encoder_in_global_config_1_test_none_input.py::test_none_input
============================== 1 failed in 0.04s ===============================
"""