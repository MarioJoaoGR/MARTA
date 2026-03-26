
import pytest
from pathlib import Path
from isort.api import _config, DEFAULT_CONFIG

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Passing both path and config_kwargs should raise ValueError
        _config(path=Path("some/path"), config=DEFAULT_CONFIG, settings_file="some_file.toml")

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

isort/Test4DT_tests/test_isort_api__config_1_test_invalid_inputs.py F    [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            # Passing both path and config_kwargs should raise ValueError
>           _config(path=Path("some/path"), config=DEFAULT_CONFIG, settings_file="some_file.toml")

isort/Test4DT_tests/test_isort_api__config_1_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/api.py:658: in _config
    config = Config(**config_kwargs)
isort/isort/settings.py:321: in __init__
    config_settings = _get_config_data(
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'some_file.toml', sections = ('isort', 'tool:isort', 'tool.isort')

    def _get_config_data(file_path: str, sections: tuple[str, ...]) -> dict[str, Any]:
        settings: dict[str, Any] = {}
    
        if file_path.endswith(".toml"):
>           with open(file_path, "rb") as bin_config_file:
E           FileNotFoundError: [Errno 2] No such file or directory: 'some_file.toml'

isort/isort/settings.py:824: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__config_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================
"""