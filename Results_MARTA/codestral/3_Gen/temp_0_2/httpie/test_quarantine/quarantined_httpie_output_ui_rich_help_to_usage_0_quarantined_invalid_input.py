
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_help import to_usage, ParserSpec, RenderableType
from typing import Optional, AbstractSet

@pytest.mark.parametrize("invalid_input", [None, 123, {}])
def test_invalid_input(invalid_input):
    spec = ParserSpec()
    with pytest.raises(TypeError):
        to_usage(spec, program_name=invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_rich_help_to_usage_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_help_to_usage_0_test_invalid_input.py:9:11: E1120: No value for argument 'program' in constructor call (no-value-for-parameter)


"""