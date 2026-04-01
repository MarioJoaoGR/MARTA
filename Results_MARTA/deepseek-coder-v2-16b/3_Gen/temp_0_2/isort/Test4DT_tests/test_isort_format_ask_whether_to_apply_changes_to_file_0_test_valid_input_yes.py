
import sys
from unittest.mock import patch
import pytest

def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
    """
    Prompts the user to decide whether to apply suggested changes to a file.
    
    The function presents a prompt asking if the user wants to apply changes to the specified file, 
    and allows for responses of 'yes' (or 'y'), 'no' (or 'n'), or 'quit' (or 'q'). If the user inputs 'no' 
    or 'n', the function returns False. If the user inputs 'quit' or 'q', the program exits with a status code of 1.
    
    Parameters:
        file_path (str): The path to the file for which changes are suggested. This string is used in the prompt message.
        
    Returns:
        bool: True if the user inputs 'yes' or 'y', False otherwise. If the user inputs 'quit' or 'q', the program exits.
    
    Example:
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

@pytest.mark.parametrize("user_input, expected_output", [('y', True), ('Y', True), ('yes', True)])
def test_valid_input_yes(user_input, expected_output):
    with patch('builtins.input', side_effect=user_input):
        assert ask_whether_to_apply_changes_to_file("example.txt") == expected_output
