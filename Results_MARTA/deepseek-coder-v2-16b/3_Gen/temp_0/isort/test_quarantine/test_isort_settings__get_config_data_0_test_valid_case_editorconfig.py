
import pytest
from isort.settings import _get_config_data

@pytest.mark.parametrize("file_path, sections, expected", [
    ("path/to/tomlfile.toml", ("section1", "section2"), {"section1": {}, "section2": {}}),
    ("path/to/editorconfigfile", ("*.{ext}", "section3"), {"section3": {}})
])
def test_get_config_data(file_path, sections, expected):
    config_data = _get_config_data(file_path, sections)
    assert config_data == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_editorconfig.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______ test_get_config_data[path/to/tomlfile.toml-sections0-expected0] ________

file_path = 'path/to/tomlfile.toml', sections = ('section1', 'section2')
expected = {'section1': {}, 'section2': {}}

    @pytest.mark.parametrize("file_path, sections, expected", [
        ("path/to/tomlfile.toml", ("section1", "section2"), {"section1": {}, "section2": {}}),
        ("path/to/editorconfigfile", ("*.{ext}", "section3"), {"section3": {}})
    ])
    def test_get_config_data(file_path, sections, expected):
>       config_data = _get_config_data(file_path, sections)

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_editorconfig.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'path/to/tomlfile.toml', sections = ('section1', 'section2')

    def _get_config_data(file_path: str, sections: tuple[str, ...]) -> dict[str, Any]:
        settings: dict[str, Any] = {}
    
        if file_path.endswith(".toml"):
>           with open(file_path, "rb") as bin_config_file:
E           FileNotFoundError: [Errno 2] No such file or directory: 'path/to/tomlfile.toml'

isort/isort/settings.py:824: FileNotFoundError
______ test_get_config_data[path/to/editorconfigfile-sections1-expected1] ______

file_path = 'path/to/editorconfigfile', sections = ('*.{ext}', 'section3')
expected = {'section3': {}}

    @pytest.mark.parametrize("file_path, sections, expected", [
        ("path/to/tomlfile.toml", ("section1", "section2"), {"section1": {}, "section2": {}}),
        ("path/to/editorconfigfile", ("*.{ext}", "section3"), {"section3": {}})
    ])
    def test_get_config_data(file_path, sections, expected):
>       config_data = _get_config_data(file_path, sections)

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_editorconfig.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'path/to/editorconfigfile', sections = ('*.{ext}', 'section3')

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
E           FileNotFoundError: [Errno 2] No such file or directory: 'path/to/editorconfigfile'

isort/isort/settings.py:832: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_editorconfig.py::test_get_config_data[path/to/tomlfile.toml-sections0-expected0]
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_editorconfig.py::test_get_config_data[path/to/editorconfigfile-sections1-expected1]
============================== 2 failed in 0.13s ===============================
"""