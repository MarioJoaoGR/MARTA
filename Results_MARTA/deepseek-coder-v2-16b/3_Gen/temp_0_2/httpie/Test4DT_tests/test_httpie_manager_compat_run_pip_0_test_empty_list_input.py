
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.compat import run_pip as original_run_pip

@pytest.fixture(autouse=True)
def mock_run_pip():
    with patch('httpie.manager.compat.run_pip', autospec=True) as mock_run_pip:
        yield mock_run_pip

def test_empty_list_input():
    # Arrange
    args = []
    
    # Act
    result = original_run_pip(args)
    
    # Assert
    assert result is not None, "Expected non-None output"
