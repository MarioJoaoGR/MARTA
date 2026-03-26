
import pytest
from isort.settings import _get_config_data

def test_invalid_file_extension():
    with pytest.raises(ValueError) as excinfo:
        _get_config_data("path/to/invalid_file.ext", ("section1", "section2"))
    assert str(excinfo.value) == "Unsupported file extension 'ext'. Only '.toml' and '.ini' files are supported."

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
        with pytest.raises(ValueError) as excinfo:
>           _get_config_data("path/to/invalid_file.ext", ("section1", "section2"))

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_file_extension.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'path/to/invalid_file.ext', sections = ('section1', 'section2')

    def _get_config_data(file_path: str, sections: tuple[str, ...]) -> dict[str, Any]:
        settings: dict[str, Any] = {}
    
        if file_path.endswith(".toml"):
            with open(file_path, "rb") as bin_config_file:
                config = tomllib.load(bin_config_file)
            for section in sections:
                config_section = config
                for key in section.split("."):
                    config_section = config_section.get(key, {})
                settings.update(config_section)
        else:
>           with open(file_path, encoding="utf-8") as config_file:
E           FileNotFoundError: [Errno 2] No such file or directory: 'path/to/invalid_file.ext'

isort/isort/settings.py:832: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_invalid_file_extension.py::test_invalid_file_extension
============================== 1 failed in 0.11s ===============================
"""