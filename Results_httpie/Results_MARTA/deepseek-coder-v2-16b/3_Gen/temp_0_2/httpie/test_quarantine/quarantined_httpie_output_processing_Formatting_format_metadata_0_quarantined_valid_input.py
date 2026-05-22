
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting
from httpie.environment import Environment

@pytest.fixture
def setup_formatting():
    groups = ['html', 'csv']
    env = Environment()
    kwargs = {}
    return Formatting(groups, env, **kwargs)

def test_valid_input(setup_formatting):
    # Arrange
    formatting = setup_formatting
    metadata = "raw_metadata"
    
    # Create mock formatters with enabled=True for testing
    formatter1 = MagicMock()
    formatter2 = MagicMock()
    
    with patch('httpie.output.processing.plugin_manager') as plugin_mock:
        plugin_mock.get_formatters_grouped.return_value = {
            'html': [formatter1],
            'csv': [formatter2]
        }
        
        # Act
        formatted_metadata = formatting.format_metadata(metadata)
        
        # Assert
        assert formatter1.format_metadata.call_count == 1
        assert formatter2.format_metadata.call_count == 1
        assert formatted_metadata == "raw_metadata"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_processing_Formatting_format_metadata_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_metadata_0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_metadata_0_test_valid_input.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""