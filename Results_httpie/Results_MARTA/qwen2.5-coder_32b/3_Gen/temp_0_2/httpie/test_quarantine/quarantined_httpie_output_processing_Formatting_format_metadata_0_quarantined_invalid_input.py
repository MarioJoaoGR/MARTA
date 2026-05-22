
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.processing import Formatting
from httpie.environment import Environment

def test_invalid_input():
    with patch('httpie.output.processing.plugin_manager.get_formatters_grouped', return_value={}):
        formatting = Formatting(groups=['html', 'csv'], env=Environment())
        assert formatting.enabled_plugins == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_processing_Formatting_format_metadata_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting_format_metadata_0_test_invalid_input.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting_format_metadata_0_test_invalid_input.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""