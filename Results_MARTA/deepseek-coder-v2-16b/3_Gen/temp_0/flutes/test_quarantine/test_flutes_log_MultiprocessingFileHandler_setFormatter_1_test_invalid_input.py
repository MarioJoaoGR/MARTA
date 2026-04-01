
import pytest
from unittest.mock import patch
from pathlib import Path
from flutes.log import MultiprocessingFileHandler

def test_invalid_input():
    with patch('flutes.log.MultiprocessingFileHandler.setFormatter') as mock_setFormatter:
        handler = MultiprocessingFileHandler(Path("logs/app.log"))
        
        # Mocking the setFormatter method to raise a TypeError when an integer is passed
        mock_setFormatter.side_effect = TypeError("Expected a string, got int instead.")
        
        with pytest.raises(TypeError) as excinfo:
            handler.setFormatter(123)  # Passing an integer instead of a string
            
        assert str(excinfo.value) == "Expected a string, got int instead."
