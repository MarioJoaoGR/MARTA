
import pytest

from isort.exceptions import ExistingSyntaxErrors


def test_valid_input():
    """
    Test to check if ExistingSyntaxErrors is raised correctly when provided with a valid file path.
    """
    # Define a valid file path for testing
    valid_file_path = "example_code.py"
    
    # Use pytest's raises function to assert that the exception is raised
    with pytest.raises(ExistingSyntaxErrors) as exc_info:
        raise ExistingSyntaxErrors(valid_file_path)
    
    # Assert that the exception message contains the provided file path
    assert str(exc_info.value) == f"isort was told to sort imports within code that contains syntax errors: {valid_file_path}."
