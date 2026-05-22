
import pytest
from httpie.plugins.base import Environment

@pytest.fixture
def env():
    return Environment()

@pytest.fixture
def formatter_plugin(env):
    format_options = {'style': 'pretty'}
    return FormatterPlugin(env=env, format_options=format_options)

def test_valid_inputs(formatter_plugin):
    assert formatter_plugin.enabled is True
    assert isinstance(formatter_plugin.kwargs, dict)
    assert isinstance(formatter_plugin.format_options, dict)
    assert formatter_plugin.format_options['style'] == 'pretty'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs.py:3:0: E0611: No name 'Environment' in module 'httpie.plugins.base' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs.py:12:11: E0602: Undefined variable 'FormatterPlugin' (undefined-variable)


"""