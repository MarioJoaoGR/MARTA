
import pytest
from unittest.mock import patch
import os

# Assuming get_file_content is a function that reads file content, which we will mock for testing purposes
def get_file_content(path, strip=True):
    with open(path, 'r') as f:
        lines = f.readlines()
        if strip:
            lines = [line.strip() for line in lines]
        return "\n".join(lines)

# Mocking get_file_content to avoid actual file reading during tests
@patch('your_module_name.get_file_content')
def test_valid_input_stripped(mock_get_file_content, tmpdir):
    mock_get_file_content.return_value = "line1\nline2\nline3"
    path = os.path.join(tmpdir, 'example.txt')
    with open(path, 'w') as f:
        f.write("line1\nline2\nline3")
    
    from your_module_name import get_file_lines
    result = get_file_lines(path)
    assert result == ['line1', 'line2', 'line3']

@patch('your_module_name.get_file_content')
def test_invalid_path(_):
    from your_module_name import get_file_lines
    with pytest.raises(FileNotFoundError):
        get_file_lines("nonexistent_file.txt")

@patch('your_module_name.get_file_content')
def test_no_strip(mock_get_file_content, tmpdir):
    mock_get_file_content.return_value = " line1\n line2\n line3"
    path = os.path.join(tmpdir, 'example.txt')
    with open(path, 'w') as f:
        f.write(" line1\n line2\n line3")
    
    from your_module_name import get_file_lines
    result = get_file_lines(path, strip=False)
    assert result == [' line1', ' line2', ' line3']
