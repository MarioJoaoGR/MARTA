
import pytest
from pathlib import Path
import io
from flutes.io import reverse_open

# Assuming the function `reverse_open` is correctly implemented and available in the module 'flutes.io'

def test_reverse_open_basic():
    # Test basic functionality with a sample file
    content = "Line 1\nLine 2\nLine 3"
    path = Path("testfile.txt")
    path.write_text(content)
    
    with reverse_open(path, encoding='utf-8', allow_empty_lines=True) as f:
        lines = [line.rstrip() for line in f]  # Use rstrip to remove any trailing whitespace including newline
    
    assert lines == ['Line 3', 'Line 2', 'Line 1']
    path.unlink()

def test_reverse_open_empty():
    # Test with an empty file
    content = ""
    path = Path("testfile.txt")
    path.write_text(content)
    
    with reverse_open(path, encoding='utf-8', allow_empty_lines=True) as f:
        lines = [line.rstrip() for line in f]  # Use rstrip to remove any trailing whitespace including newline
    
    assert lines == []
    path.unlink()

def test_reverse_open_no_allow_empty():
    # Test without allowing empty lines
    content = "Line 1\n\nLine 3"
    path = Path("testfile.txt")
    path.write_text(content)
    
    with reverse_open(path, encoding='utf-8', allow_empty_lines=False) as f:
        lines = [line.rstrip() for line in f]  # Use rstrip to remove any trailing whitespace including newline
    
    assert lines == ['Line 3', 'Line 1']
    path.unlink()

def test_reverse_open_invalid_buffer():
    # Test with an invalid buffer size
    content = "Test line"
    path = Path("testfile.txt")
    path.write_text(content)
    
    with pytest.raises(ValueError):
        reverse_open(path, encoding='utf-8', allow_empty_lines=True, buffer_size=1)
    
    path.unlink()
