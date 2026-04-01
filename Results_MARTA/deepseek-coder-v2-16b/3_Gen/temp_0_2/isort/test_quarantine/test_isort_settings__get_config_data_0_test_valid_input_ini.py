
import pytest
from isort.settings import _get_config_data

@pytest.fixture
def valid_ini_file(tmp_path):
    ini_file = tmp_path / "test.ini"
    with open(ini_file, "w") as f:
        f.write("[section1]\nkey1=value1\nkey2=value2\n")
        f.write("[section2]\nkey3=value3\n")
    return str(ini_file)

def test_valid_input_ini(valid_ini_file):
    sections = ("section1", "section2")
    config_data = _get_config_data(valid_ini_file, sections)
    
    assert isinstance(config_data, dict)
    assert "source" in config_data
    assert config_data["source"] == str(valid_ini_file)
    assert config_data == {
        "key1": "value1",
        "key2": "value2",
        "section2.key3": "value3",
        "source": str(valid_ini_file)
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
collected 1 item

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_input_ini.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_input_ini _____________________________

valid_ini_file = '/tmp/pytest-of-joaovitorino/pytest-4/test_valid_input_ini0/test.ini'

    def test_valid_input_ini(valid_ini_file):
        sections = ("section1", "section2")
        config_data = _get_config_data(valid_ini_file, sections)
    
        assert isinstance(config_data, dict)
        assert "source" in config_data
        assert config_data["source"] == str(valid_ini_file)
>       assert config_data == {
            "key1": "value1",
            "key2": "value2",
            "section2.key3": "value3",
            "source": str(valid_ini_file)
        }
E       AssertionError: assert {'key1': 'val...ni0/test.ini'} == {'key1': 'val...ni0/test.ini'}
E         
E         Omitting 3 identical items, use -vv to show
E         Left contains 1 more item:
E         {'key3': 'value3'}
E         Right contains 1 more item:
E         {'section2.key3': 'value3'}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_input_ini.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_input_ini.py::test_valid_input_ini
============================== 1 failed in 0.11s ===============================
"""