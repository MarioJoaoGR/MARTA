
import pytest
from httpie.plugins.base import FormatterPlugin

def test_valid_input():
    # Arrange
    env = Environment()  # Assuming an Environment class is defined elsewhere
    format_options = {'style': 'pretty'}
    
    # Act
    formatter = FormatterPlugin(env=env, format_options=format_options)
    
    # Assert
    assert isinstance(formatter, FormatterPlugin)
    assert formatter.enabled is True
    assert formatter.format_options == {'style': 'pretty'}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_base_FormatterPlugin_format_metadata_1_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_plugins_base_FormatterPlugin_format_metadata_1_test_valid_input.py:7:10: E0602: Undefined variable 'Environment' (undefined-variable)


"""