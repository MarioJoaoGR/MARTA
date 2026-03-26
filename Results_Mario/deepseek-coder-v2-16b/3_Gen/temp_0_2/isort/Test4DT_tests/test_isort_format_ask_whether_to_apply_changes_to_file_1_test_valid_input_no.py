
import sys
from unittest.mock import patch
from isort.format import ask_whether_to_apply_changes_to_file

def test_valid_input_no():
    with patch('builtins.input', side_effect=['n']):
        assert not ask_whether_to_apply_changes_to_file("example.txt")

# If you need to mock the sys.exit function as well, you can do so like this:
def test_valid_input_quit():
    with patch('builtins.input', side_effect=['q']):
        with patch('sys.exit') as mock_exit:
            ask_whether_to_apply_changes_to_file("example.txt")
            mock_exit.assert_called_with(1)
