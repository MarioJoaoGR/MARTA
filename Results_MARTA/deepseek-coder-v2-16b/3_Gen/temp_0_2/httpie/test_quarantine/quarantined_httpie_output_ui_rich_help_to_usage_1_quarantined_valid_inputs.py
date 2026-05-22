
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_help import to_usage, ParserSpec, RenderableType
from typing import Optional, AbstractSet

@pytest.mark.parametrize("program_name", [None, "my_program"])
def test_to_usage(program_name):
    spec = ParserSpec()
    whitelist = frozenset(["-w", "--whitelist"])
    
    with patch('httpie.output.ui.rich_help.Text', autospec=True) as mock_text:
        result = to_usage(spec, program_name=program_name, whitelist=whitelist)
        
        assert isinstance(result, RenderableType)
        mock_text.assert_called_once_with(program_name or spec.program, style='bold')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_rich_help_to_usage_1_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_to_usage_1_test_valid_inputs.py:9:11: E1120: No value for argument 'program' in constructor call (no-value-for-parameter)


"""