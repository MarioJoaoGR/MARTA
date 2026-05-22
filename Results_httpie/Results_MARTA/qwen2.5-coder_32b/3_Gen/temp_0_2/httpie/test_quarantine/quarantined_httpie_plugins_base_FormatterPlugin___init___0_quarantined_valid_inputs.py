
import pytest
from httpie.plugins.base import FormatterPlugin
from unittest.mock import patch, MagicMock

def test_valid_inputs():
    with patch('httpie.plugins.base.Environment', autospec=True):
        env = Environment()  # Assuming an Environment class is defined elsewhere
        format_options = {'style': 'pretty'}
        formatter = FormatterPlugin(env=env, format_options=format_options)
        
        assert formatter.enabled is True
        assert formatter.kwargs == {'format_options': format_options}
        assert formatter.format_options == format_options

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs.py:8:14: E0602: Undefined variable 'Environment' (undefined-variable)


"""