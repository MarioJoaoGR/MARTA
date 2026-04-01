
import pytest
from flutes.log import MultiprocessingFileHandler

def test_valid_input():
    # Arrange
    log_path = "logs/app.log"
    handler = MultiprocessingFileHandler(log_path)
    
    # Act & Assert (no need to act as we are just testing the setup)
    assert isinstance(handler, MultiprocessingFileHandler)
