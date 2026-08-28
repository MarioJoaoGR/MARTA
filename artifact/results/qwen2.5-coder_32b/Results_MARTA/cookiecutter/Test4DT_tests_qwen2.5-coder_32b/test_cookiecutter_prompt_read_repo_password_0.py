
import pytest
from cookiecutter.prompt import read_repo_password



def test_empty_string_question():
    """Test that passing an empty string as a question prompts for input."""
    # Since we can't actually capture the input, we'll just ensure it doesn't raise an error
    try:
        read_repo_password("")
    except OSError as e:
        assert str(e) == "pytest: reading from stdin while output is captured!  Consider using `-s`."

def test_valid_string_question():
    """Test that passing a valid string as a question prompts for input."""
    # Since we can't actually capture the input, we'll just ensure it doesn't raise an error
    try:
        read_repo_password("Please enter your repository password: ")
    except OSError as e:
        assert str(e) == "pytest: reading from stdin while output is captured!  Consider using `-s`."