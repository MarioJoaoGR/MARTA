
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.ui.rich_help import to_usage, ParserSpec, RenderableType

@pytest.mark.parametrize("spec, program_name, whitelist, expected", [
    (ParserSpec(), None, frozenset(), "Usage string"),  # Test case for default values
    (ParserSpec(program="test_program"), "test_program", frozenset(["arg1"]), "Usage string with specific program name and whitelist"),  # Test case with specific program name and whitelist
])
def test_to_usage(spec, program_name, whitelist, expected):
    with patch('httpie.output.ui.rich_help.Text', new=MagicMock()) as mock_text:
        usage = to_usage(spec, program_name=program_name, whitelist=whitelist)
        assert isinstance(usage, RenderableType)  # Ensure the output is of the correct type
        mock_text.assert_called_once_with("test_program", style="bold")  # Check if Text was called with the correct program name

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_rich_help_to_usage_1_test_invalid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_help_to_usage_1_test_invalid_inputs.py:7:5: E1120: No value for argument 'program' in constructor call (no-value-for-parameter)


"""