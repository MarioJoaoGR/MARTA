
import pytest
from pathlib import Path
from isort.api import _config, DEFAULT_CONFIG
from isort.settings import Config

def test_invalid_input_both_specified():
    with pytest.raises(ValueError) as excinfo:
        config = _config(path=Path('non_existent_file.toml'), settings_path='some/directory', settings_file='custom.toml')
    
    assert "You can either specify custom configuration options using kwargs or passing in a Config object. Not Both!" in str(excinfo.value)

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

isort/Test4DT_tests/test_isort_api__config_1_test_invalid_input_both_specified.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_both_specified _______________________

    def test_invalid_input_both_specified():
        with pytest.raises(ValueError) as excinfo:
>           config = _config(path=Path('non_existent_file.toml'), settings_path='some/directory', settings_file='custom.toml')

isort/Test4DT_tests/test_isort_api__config_1_test_invalid_input_both_specified.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/api.py:658: in _config
    config = Config(**config_kwargs)
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'custom.toml', sections = ('isort', 'tool:isort', 'tool.isort')

    def _get_config_data(file_path: str, sections: tuple[str, ...]) -> dict[str, Any]:
        settings: dict[str, Any] = {}
    
        if file_path.endswith(".toml"):
>           with open(file_path, "rb") as bin_config_file:
E           FileNotFoundError: [Errno 2] No such file or directory: 'custom.toml'

isort/isort/settings.py:824: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__config_1_test_invalid_input_both_specified.py::test_invalid_input_both_specified
============================== 1 failed in 0.13s ===============================
"""