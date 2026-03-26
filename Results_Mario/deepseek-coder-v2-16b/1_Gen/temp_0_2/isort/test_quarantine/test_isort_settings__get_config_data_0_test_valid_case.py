
import pytest
from isort.settings import _get_config_data

@pytest.fixture
def valid_toml_file(tmp_path):
    file_path = tmp_path / "test.toml"
    content = """
[section1]
key1 = "value1"
key2 = 42

[section2]
key3 = true
"""
    file_path.write_text(content)
    return str(file_path)

@pytest.fixture
def valid_ini_file(tmp_path):
    file_path = tmp_path / "test.ini"
    content = """
[section1]
key1 = value1
key2 = 42

[section2]
key3 = true
"""
    file_path.write_text(content)
    return str(file_path)

def test_get_config_data_valid_toml(valid_toml_file):
    config_data = _get_config_data(valid_toml_file, ("section1", "section2"))
    assert config_data == {
        'key1': 'value1',
        'key2': 42,
        'key3': True
    }

def test_get_config_data_valid_ini(valid_ini_file):
    config_data = _get_config_data(valid_ini_file, ("section1", "section2"))
    assert config_data == {
        'key1': 'value1',
        'key2': 42,
        'key3': True
    }

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

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_get_config_data_valid_toml ________________________

valid_toml_file = '/tmp/pytest-of-joaovitorino/pytest-2/test_get_config_data_valid_tom0/test.toml'

    def test_get_config_data_valid_toml(valid_toml_file):
        config_data = _get_config_data(valid_toml_file, ("section1", "section2"))
>       assert config_data == {
            'key1': 'value1',
            'key2': 42,
            'key3': True
        }
E       AssertionError: assert {'key1': 'val...m0/test.toml'} == {'key1': 'val... 'key3': True}
E         
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'key2': '42'} != {'key2': 42}
E         {'key3': 'True'} != {'key3': True}
E         Left contains 1 more item:
E         {'source': '/tmp/pytest-of-joaovitorino/pytest-2/test_get_config_data_valid_tom0/test.toml'}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case.py:35: AssertionError
________________________ test_get_config_data_valid_ini ________________________

valid_ini_file = '/tmp/pytest-of-joaovitorino/pytest-2/test_get_config_data_valid_ini0/test.ini'

    def test_get_config_data_valid_ini(valid_ini_file):
        config_data = _get_config_data(valid_ini_file, ("section1", "section2"))
>       assert config_data == {
            'key1': 'value1',
            'key2': 42,
            'key3': True
        }
E       AssertionError: assert {'key1': 'val...ni0/test.ini'} == {'key1': 'val... 'key3': True}
E         
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'key2': '42'} != {'key2': 42}
E         {'key3': 'true'} != {'key3': True}
E         Left contains 1 more item:
E         {'source': '/tmp/pytest-of-joaovitorino/pytest-2/test_get_config_data_valid_ini0/test.ini'}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case.py:43: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case.py::test_get_config_data_valid_toml
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case.py::test_get_config_data_valid_ini
============================== 2 failed in 0.11s ===============================
"""