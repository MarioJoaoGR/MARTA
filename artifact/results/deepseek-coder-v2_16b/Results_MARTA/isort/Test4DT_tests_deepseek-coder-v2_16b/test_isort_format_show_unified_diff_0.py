
import pytest
from io import StringIO
from pathlib import Path
from datetime import datetime
from isort.format import show_unified_diff, create_terminal_printer, unified_diff


def test_edge_cases():
    file_input = ""
    file_output = ""
    output = StringIO()
    show_unified_diff(file_input=file_input, file_output=file_output, file_path=None, output=output, color_output=False)
    diff_lines = output.getvalue().splitlines()
    assert len(diff_lines) == 0
