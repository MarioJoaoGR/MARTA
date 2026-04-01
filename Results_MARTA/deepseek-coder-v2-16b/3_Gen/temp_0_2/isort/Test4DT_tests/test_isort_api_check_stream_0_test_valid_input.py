
import pytest
from io import StringIO
from isort.api import check_stream, Config, DEFAULT_CONFIG

def test_valid_input():
    """Test with valid input stream and default settings."""
    # Arrange
    code = "import os\nimport sys"
    input_stream = StringIO(code)
    
    # Act
    result = check_stream(input_stream, show_diff=False, config=DEFAULT_CONFIG)
    
    # Assert
    assert result is True
