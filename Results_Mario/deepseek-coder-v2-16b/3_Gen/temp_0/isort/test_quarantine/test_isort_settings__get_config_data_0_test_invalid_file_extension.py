
import pytest
from isort.settings import _get_config_data

def test_invalid_file_extension():
    with pytest.raises(ValueError) as excinfo:
        _get_config_data("invalid_path", ("section1", "section2"))
    assert str(excinfo.value) == "Unsupported file extension for 'invalid_path'. Only '.toml' and '.editorconfig' are supported."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_file_extension.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_file_extension __________________________

    def test_invalid_file_extension():
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_file_extension.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_file_extension.py::test_invalid_file_extension
============================== 1 failed in 0.12s ===============================
"""