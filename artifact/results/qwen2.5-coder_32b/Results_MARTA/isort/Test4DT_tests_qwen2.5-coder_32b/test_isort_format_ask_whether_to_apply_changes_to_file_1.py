
import sys
from unittest.mock import patch

def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
    answer = None
    while answer not in ("yes", "y", "no", "n", "quit", "q"):
        answer = input(f"Apply suggested changes to '{file_path}' [y/n/q]? ").lower()
        if answer in ("no", "n"):
            return False
        if answer in ("quit", "q"):
            sys.exit(1)
    return True

def test_happy_path():
    with patch('builtins.input', side_effect=['y']):
        result = ask_whether_to_apply_changes_to_file('example.txt')
        assert result is True

def test_edge_case_none_input():
    with patch('builtins.input', side_effect=['', 'yes']):
        result = ask_whether_to_apply_changes_to_file(None)
        assert result is True

def test_invalid_input_handling():
    with patch('builtins.input', side_effect=['invalid', 'nope', 'n']):
        result = ask_whether_to_apply_changes_to_file('example.txt')
        assert result is False
