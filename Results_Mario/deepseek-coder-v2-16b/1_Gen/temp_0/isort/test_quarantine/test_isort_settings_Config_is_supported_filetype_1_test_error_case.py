
from isort.settings import Config
import pytest

@pytest.fixture
def config():
    return Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.tox', 'dist', '__pypackages__', 'venv', '.pants.d...ge}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=False))

def test_error_case(config):
    assert not config.is_supported_filetype('test.txt')  # Assuming 'test.txt' is an unsupported file
    assert config.is_supported_filetype('test.py')      # Assuming 'test.py' is a supported file

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_is_supported_filetype_1_test_error_case
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_1_test_error_case.py:7:251: E0001: Parsing failed: 'closing parenthesis ')' does not match opening parenthesis '{' (Test4DT_tests.test_isort_settings_Config_is_supported_filetype_1_test_error_case, line 7)' (syntax-error)


"""