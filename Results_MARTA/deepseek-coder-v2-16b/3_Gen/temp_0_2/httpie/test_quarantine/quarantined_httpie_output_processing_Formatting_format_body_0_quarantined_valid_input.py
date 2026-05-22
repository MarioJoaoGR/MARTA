
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting
from httpie.plugins import plugin_manager

@pytest.fixture
def setup_formatting():
    # Create a mock environment and plugins for testing
    env = MagicMock()
    formatters = {
        'group1': [MagicMock(), MagicMock()],
        'group2': [MagicMock()]
    }
    
    with patch('httpie.plugins.plugin_manager.get_formatters_grouped', return_value=formatters):
        formatting = Formatting(groups=['group1', 'group2'], env=env)
        yield formatting

def test_valid_input(setup_formatting):
    formatting = setup_formatting
    
    # Mock the format_body method of plugins to return a modified content
    with patch.object(formatting.enabled_plugins[0], 'format_body', return_value='formatted_content'):
        result = formatting.format_body('original_content', 'mime/type')
        
        assert result == 'formatted_content'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_processing_Formatting_format_body_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_body_0_test_valid_input.py:5:0: E0611: No name 'plugin_manager' in module 'httpie.plugins' (no-name-in-module)


"""