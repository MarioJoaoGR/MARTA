
import io
from pathlib import Path
import sys
from unittest.mock import patch, MagicMock
import pytest
from isort.format import show_unified_diff

def test_show_unified_diff_basic():
    original_content = "line1\nline2\n"
    modified_content = "line1\nline3\n"
    file_path = Path("example.txt")
    
    output_stream = io.StringIO()
    with patch('pathlib.Path.stat', return_value=MagicMock(st_mtime=0)):
        show_unified_diff(
            file_input=original_content,
            file_output=modified_content,
            file_path=file_path,
            output=output_stream
        )
    
    diff_output = output_stream.getvalue()
    assert "line2" in diff_output
    assert "-line2\n+line3\n" in diff_output

def test_show_unified_diff_no_file_path():
    original_content = "line1\nline2\n"
    modified_content = "line1\nline3\n"
    
    output_stream = io.StringIO()
    show_unified_diff(
        file_input=original_content,
        file_output=modified_content,
        file_path=None,
        output=output_stream
    )
    
    diff_output = output_stream.getvalue()
    assert ":before" in diff_output
    assert ":after" in diff_output

def test_show_unified_diff_color_output():
    original_content = "line1\nline2\n"
    modified_content = "line1\nline3\n"
    file_path = Path("example.txt")
    
    output_stream = io.StringIO()
    with patch('isort.format.create_terminal_printer') as mock_create_printer:
        mock_printer = MagicMock()
        mock_create_printer.return_value = mock_printer
        with patch('pathlib.Path.stat', return_value=MagicMock(st_mtime=0)):
            show_unified_diff(
                file_input=original_content,
                file_output=modified_content,
                file_path=file_path,
                output=output_stream,
                color_output=True
            )
    
    mock_create_printer.assert_called_once_with(True, output_stream)
    assert not output_stream.getvalue()

def test_show_unified_diff_no_changes():
    original_content = "line1\nline2\n"
    modified_content = "line1\nline2\n"
    file_path = Path("example.txt")
    
    output_stream = io.StringIO()
    with patch('pathlib.Path.stat', return_value=MagicMock(st_mtime=0)):
        show_unified_diff(
            file_input=original_content,
            file_output=modified_content,
            file_path=file_path,
            output=output_stream
        )
    
    diff_output = output_stream.getvalue()