
import pytest
from httpie.plugins.base import Environment

@pytest.fixture
def formatter_plugin():
    env = Environment()
    format_options = {'style': 'pretty'}
    return FormatterPlugin(env=env, format_options=format_options)

def test_edge_case(formatter_plugin):
    metadata = "Some metadata text"
    formatted_metadata = formatter_plugin.format_metadata(metadata)
    assert formatted_metadata == metadata

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_base_FormatterPlugin_format_metadata_0_test_edge_case
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin_format_metadata_0_test_edge_case.py:3:0: E0611: No name 'Environment' in module 'httpie.plugins.base' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin_format_metadata_0_test_edge_case.py:9:11: E0602: Undefined variable 'FormatterPlugin' (undefined-variable)


"""