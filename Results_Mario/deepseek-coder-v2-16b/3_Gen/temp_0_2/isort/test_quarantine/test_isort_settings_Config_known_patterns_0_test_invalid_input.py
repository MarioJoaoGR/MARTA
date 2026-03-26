
import pytest
from isort.settings import Config
from isort.exceptions import InvalidSettingsPath

class TestConfig:
    @pytest.mark.parametrize("invalid_input", [
        "",  # Empty string
        "nonexistentfile.toml",  # Non-existent file
        "/non/existent/directory/",  # Non-existent directory
    ])
    def test_invalid_config_file(self, invalid_input):
        with pytest.raises(FileNotFoundError) as excinfo:
            Config(settings_file=invalid_input)
        assert str(excinfo.value).endswith("No such file or directory")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________ TestConfig.test_invalid_config_file[] _____________________

self = <Test4DT_tests.test_isort_settings_Config_known_patterns_0_test_invalid_input.TestConfig object at 0x7fcd57ce8850>
invalid_input = ''

    @pytest.mark.parametrize("invalid_input", [
        "",  # Empty string
        "nonexistentfile.toml",  # Non-existent file
        "/non/existent/directory/",  # Non-existent directory
    ])
    def test_invalid_config_file(self, invalid_input):
>       with pytest.raises(FileNotFoundError) as excinfo:
E       Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py:13: Failed
__________ TestConfig.test_invalid_config_file[nonexistentfile.toml] ___________

self = <Test4DT_tests.test_isort_settings_Config_known_patterns_0_test_invalid_input.TestConfig object at 0x7fcd57ce97d0>
invalid_input = 'nonexistentfile.toml'

    @pytest.mark.parametrize("invalid_input", [
        "",  # Empty string
        "nonexistentfile.toml",  # Non-existent file
        "/non/existent/directory/",  # Non-existent directory
    ])
    def test_invalid_config_file(self, invalid_input):
        with pytest.raises(FileNotFoundError) as excinfo:
            Config(settings_file=invalid_input)
>       assert str(excinfo.value).endswith("No such file or directory")
E       assert False
E        +  where False = <built-in method endswith of str object at 0x7fcd57d191b0>('No such file or directory')
E        +    where <built-in method endswith of str object at 0x7fcd57d191b0> = "[Errno 2] No such file or directory: 'nonexistentfile.toml'".endswith
E        +      where "[Errno 2] No such file or directory: 'nonexistentfile.toml'" = str(FileNotFoundError(2, 'No such file or directory'))
E        +        where FileNotFoundError(2, 'No such file or directory') = <ExceptionInfo FileNotFoundError(2, 'No such file or directory') tblen=3>.value

isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py:15: AssertionError
________ TestConfig.test_invalid_config_file[/non/existent/directory/] _________

self = <Test4DT_tests.test_isort_settings_Config_known_patterns_0_test_invalid_input.TestConfig object at 0x7fcd57ce9910>
invalid_input = '/non/existent/directory/'

    @pytest.mark.parametrize("invalid_input", [
        "",  # Empty string
        "nonexistentfile.toml",  # Non-existent file
        "/non/existent/directory/",  # Non-existent directory
    ])
    def test_invalid_config_file(self, invalid_input):
        with pytest.raises(FileNotFoundError) as excinfo:
            Config(settings_file=invalid_input)
>       assert str(excinfo.value).endswith("No such file or directory")
E       assert False
E        +  where False = <built-in method endswith of str object at 0x7fcd57d19450>('No such file or directory')
E        +    where <built-in method endswith of str object at 0x7fcd57d19450> = "[Errno 2] No such file or directory: '/non/existent/directory/'".endswith
E        +      where "[Errno 2] No such file or directory: '/non/existent/directory/'" = str(FileNotFoundError(2, 'No such file or directory'))
E        +        where FileNotFoundError(2, 'No such file or directory') = <ExceptionInfo FileNotFoundError(2, 'No such file or directory') tblen=3>.value

isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py::TestConfig::test_invalid_config_file[]
FAILED isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py::TestConfig::test_invalid_config_file[nonexistentfile.toml]
FAILED isort/Test4DT_tests/test_isort_settings_Config_known_patterns_0_test_invalid_input.py::TestConfig::test_invalid_config_file[/non/existent/directory/]
============================== 3 failed in 0.11s ===============================
"""