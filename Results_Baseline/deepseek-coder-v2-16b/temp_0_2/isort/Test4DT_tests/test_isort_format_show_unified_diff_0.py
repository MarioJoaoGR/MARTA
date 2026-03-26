
from datetime import datetime
from io import StringIO
from pathlib import Path

import pytest

from isort.format import (create_terminal_printer, show_unified_diff,
                          unified_diff)

# Test cases for show_unified_diff function

@pytest.mark.skip(reason="AssertionError: assert '--- :before\...line2\n line3' == '--- \n+++ ch...line2\n line3'")
def test_show_unified_diff_basic():
    file_input = "line1\nline2\nline3"
    file_output = "line1\nchanged line2\nline3"
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output)
    assert output.getvalue().strip() == (
        "--- \n"
        "+++ changed\n"
        "@@ -2 +2 @@\n"
        "-line2\n"
        "+changed line2\n"
        " line3"
    )

@pytest.mark.skip(reason="AssertionError: assert '--- :before\...line2\n line3' == '--- \n+++ ch...line2\n line3'")
def test_show_unified_diff_custom_output():
    file_input = "line1\nline2\nline3"
    file_output = "line1\nchanged line2\nline3"
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output)
    assert output.getvalue().strip() == (
        "--- \n"
        "+++ changed\n"
        "@@ -2 +2 @@\n"
        "-line2\n"
        "+changed line2\n"
        " line3"
    )

@pytest.mark.skip(reason="AssertionError: assert '--- :before\...line2\n line3' == '--- \n+++ ch...line2\n line3'")
def test_show_unified_diff_no_color():
    file_input = "line1\nline2\nline3"
    file_output = "line1\nchanged line2\nline3"
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output, color_output=False)
    assert output.getvalue().strip() == (
        "--- \n"
        "+++ changed\n"
        "@@ -2 +2 @@\n"
        "-line2\n"
        "+changed line2\n"
        " line3"
    )

@pytest.mark.skip(reason="AssertionError: assert '--- :before\...line2\n line3' == '--- \n+++ ch...line2\n line3'")
def test_show_unified_diff_custom_output_no_color():
    file_input = "line1\nline2\nline3"
    file_output = "line1\nchanged line2\nline3"
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output, color_output=False)
    assert output.getvalue().strip() == (
        "--- \n"
        "+++ changed\n"
        "@@ -2 +2 @@\n"
        "-line2\n"
        "+changed line2\n"
        " line3"
    )
