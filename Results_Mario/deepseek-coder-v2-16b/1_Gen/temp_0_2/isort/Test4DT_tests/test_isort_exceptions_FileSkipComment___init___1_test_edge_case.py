
import pytest
from isort.exceptions import FileSkipComment

def test_edge_case():
    # Define a mock file path for demonstration purposes
    file_path = "mock/file/path.py"
    
    # Use pytest to check if the exception is raised with the correct message
    with pytest.raises(FileSkipComment) as exc_info:
        raise FileSkipComment(file_path)
    
    # Assert that the exception message matches the expected message
    assert str(exc_info.value) == f"{file_path} contains a file skip comment and was skipped."
