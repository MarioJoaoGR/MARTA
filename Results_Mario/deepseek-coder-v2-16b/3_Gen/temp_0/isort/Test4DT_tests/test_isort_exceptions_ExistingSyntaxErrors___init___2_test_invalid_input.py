
import pytest
from isort.exceptions import ExistingSyntaxErrors

def test_invalid_input():
    """
    Test to check if ExistingSyntaxErrors is raised when an invalid (non-string) value is passed as file_path.
    """
    with pytest.raises(ExistingSyntaxErrors):
        raise ExistingSyntaxErrors(12345)  # Passing an integer instead of a string
