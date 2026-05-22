
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.ui.rich_utils import Console, Highlighter

def enable_highlighter(
    console: Console,
    highlighter: Highlighter,
) -> Iterator[Console]:
    """Enable a highlighter temporarily."""

    original_highlighter = console.highlighter
    try:
        console.highlighter = highlighter
        yield console
    finally:
        console.highlighter = original_highlighter

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_valid_input.py:9:5: E0602: Undefined variable 'Iterator' (undefined-variable)


"""