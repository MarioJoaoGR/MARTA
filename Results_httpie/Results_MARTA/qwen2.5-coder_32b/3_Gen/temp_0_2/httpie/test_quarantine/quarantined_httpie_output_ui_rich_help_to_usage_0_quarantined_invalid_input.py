
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_help import to_usage, ParserSpec, RenderableType
from typing import Optional, AbstractSet

@pytest.mark.parametrize("spec, program_name, whitelist, expected", [
    (ParserSpec(), None, frozenset(), "Usage string for default spec"),
    (ParserSpec(program="my_program"), "my_program", frozenset(["arg1"]), "Usage string for my_program with whitelist")
])
def test_to_usage(spec, program_name, whitelist, expected):
    with patch('httpie.output.ui.rich_help.Text', autospec=True) as mock_text:
        result = to_usage(spec, program_name=program_name, whitelist=whitelist)
        assert isinstance(result, RenderableType)
        # Add assertions to check the content of the usage string if needed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_ui_rich_help_to_usage_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_help_to_usage_0_test_invalid_input.py:8:5: E1120: No value for argument 'program' in constructor call (no-value-for-parameter)


"""