
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.base import Environment

@pytest.mark.parametrize("invalid_input", [None, 123, {}])
def test_format_metadata_invalid_input(invalid_input):
    env = Environment()
    formatter = FormatterPlugin(env=env, format_options={'style': 'pretty'})
    
    with patch.object(formatter, 'format_options', {'style': 'pretty'}, create=True):
        with pytest.raises(TypeError) as excinfo:
            formatter.format_metadata(invalid_input)
        
        assert "Expected str, got" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_base_FormatterPlugin_format_metadata_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_plugins_base_FormatterPlugin_format_metadata_0_test_invalid_input.py:4:0: E0611: No name 'Environment' in module 'httpie.plugins.base' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_plugins_base_FormatterPlugin_format_metadata_0_test_invalid_input.py:9:16: E0602: Undefined variable 'FormatterPlugin' (undefined-variable)


"""