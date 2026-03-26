
import sys
from unittest.mock import patch
import pytest

def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
    """
    Prompts the user to confirm whether to apply suggested changes to a file. The function ensures that the user's input is valid 
    (either 'y', 'yes', 'n', 'no', 'q', or 'quit') before returning True for 'y' and 'yes', False for 'n' and 'no', and exits the program if 'q' or 'quit' is entered.
    
    Parameters:
        file_path (str): The path to the file for which changes are suggested.
        
    Returns:
        bool: True if the user confirms to apply the changes, False otherwise. If the user decides to quit, the function will exit the program with a system exit code of 1.
        
    Examples:
        >>> ask_whether_to_apply_changes_to_file("example.txt")
        Apply suggested changes to 'example.txt' [y/n/q]? y
        True
        
        >>> ask_whether_to_apply_changes_to_file("example.txt")
        Apply suggested changes to 'example.txt' [y/n/q]? n
        False
        
        >>> ask_whether_to_apply_changes_to_file("example.txt")
        Apply suggested changes to 'example.txt' [y/n/q]? q
        Traceback (most recent call last):
            ...
        SystemExit: 1
    """
    answer = None
    while answer not in ("yes", "y", "no", "n", "quit", "q"):
        answer = input(f"Apply suggested changes to '{file_path}' [y/n/q]? ")  # nosec
        answer = answer.lower()
        if answer in ("no", "n"):
            return False
        if answer in ("quit", "q"):
            sys.exit(1)
    return True

@pytest.mark.parametrize("user_input, expected_output", [('n', False), ('N', False)])
def test_valid_input_no(user_input, expected_output):
    with patch('builtins.input', side_effect=user_input):
        assert ask_whether_to_apply_changes_to_file("example.txt") == expected_output
