
import pytest
from isort.settings import _get_config_data

def test_invalid_inputs():
    # Test with a non-existent file path
    with pytest.raises(FileNotFoundError):
        _get_config_data("nonexistentfile.toml", ("section1",))
    
    # Test with an unsupported file extension
    with open("testfile.txt", "w") as f:
        f.write("[section1]\nkey=value")
    with pytest.raises(ValueError):
        _get_config_data("testfile.txt", ("section1",))
    
    # Test with an empty file path
    with pytest.raises(FileNotFoundError):
        _get_config_data("", ("section1",))
    
    # Clean up the test file created above
    import os
    if os.path.exists("testfile.txt"):
        os.remove("testfile.txt")

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

isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        # Test with a non-existent file path
        with pytest.raises(FileNotFoundError):
            _get_config_data("nonexistentfile.toml", ("section1",))
    
        # Test with an unsupported file extension
        with open("testfile.txt", "w") as f:
            f.write("[section1]\nkey=value")
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_invalid_inputs.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.14s ===============================
"""