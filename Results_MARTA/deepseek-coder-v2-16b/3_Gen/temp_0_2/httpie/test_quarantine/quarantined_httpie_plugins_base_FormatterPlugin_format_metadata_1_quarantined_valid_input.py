
import pytest
from httpie.plugins.base import FormatterPlugin

@pytest.fixture
def formatter():
    env = Environment()  # Assuming an Environment class is defined elsewhere
    format_options = {'style': 'pretty'}
    return FormatterPlugin(env=env, format_options=format_options)

def test_valid_input(formatter):
    metadata = "Some valid metadata text"
    formatted_metadata = formatter.format_metadata(metadata)
    assert formatted_metadata == metadata

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_base_FormatterPlugin_format_metadata_1_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin_format_metadata_1_test_valid_input.py:7:10: E0602: Undefined variable 'Environment' (undefined-variable)


"""