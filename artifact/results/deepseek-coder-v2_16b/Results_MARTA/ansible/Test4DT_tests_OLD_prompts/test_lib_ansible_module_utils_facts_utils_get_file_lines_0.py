
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.utils import get_file_lines

def test_valid_input_default_strip():
    with patch('ansible.module_utils.facts.utils.get_file_content', return_value="line1\nline2\nline3"):
        result = get_file_lines('mocked_path')
        assert result == ['line1', 'line2', 'line3']

def test_valid_input_no_strip():
    with patch('ansible.module_utils.facts.utils.get_file_content', return_value=" line1 \n line2 \n line3 "):
        result = get_file_lines('mocked_path', strip=False)
        assert result == [' line1 ', ' line2 ', ' line3 ']

def test_invalid_path():
    with patch('ansible.module_utils.facts.utils.get_file_content', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            get_file_lines('non_existent_path')
