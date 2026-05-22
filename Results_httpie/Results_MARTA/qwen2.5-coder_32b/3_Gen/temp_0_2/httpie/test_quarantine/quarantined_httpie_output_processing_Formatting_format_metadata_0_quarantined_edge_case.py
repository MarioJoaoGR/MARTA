
import pytest
from httpie.output.processing import Formatting, Environment
from unittest.mock import patch

@pytest.fixture
def setup_formatting():
    groups = ['html', 'csv']
    env = Environment()
    kwargs = {}
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped') as mock_get_formatters:
        mock_get_formatters.return_value = {'html': [MockFormatter], 'csv': [MockFormatter]}
        formatting = Formatting(groups, env, **kwargs)
    return formatting

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_processing_Formatting_format_metadata_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting_format_metadata_0_test_edge_case.py:12:53: E0602: Undefined variable 'MockFormatter' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting_format_metadata_0_test_edge_case.py:12:77: E0602: Undefined variable 'MockFormatter' (undefined-variable)


"""