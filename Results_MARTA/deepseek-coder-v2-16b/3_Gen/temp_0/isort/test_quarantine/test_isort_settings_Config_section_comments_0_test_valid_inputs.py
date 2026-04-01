
from isort.settings import Config
import pytest

@pytest.fixture
def valid_config():
    return Config(py_version='py3', force_to_top=frozenset(), skip=frozenset({'.tox', 'buck-out', '.pants.d', '__pypackages__', '...age}', format_success='{success}: {message}', sort_order='natural', sort_reexports=False, split_on_trailing_comma=True)

def test_valid_inputs(valid_config):
    assert valid_config.section_comments() == ('# standard', '# third_party', '# first_party', '# local_folder')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_section_comments_0_test_valid_inputs
isort/Test4DT_tests/test_isort_settings_Config_section_comments_0_test_valid_inputs.py:7:251: E0001: Parsing failed: 'closing parenthesis ')' does not match opening parenthesis '{' (Test4DT_tests.test_isort_settings_Config_section_comments_0_test_valid_inputs, line 7)' (syntax-error)


"""