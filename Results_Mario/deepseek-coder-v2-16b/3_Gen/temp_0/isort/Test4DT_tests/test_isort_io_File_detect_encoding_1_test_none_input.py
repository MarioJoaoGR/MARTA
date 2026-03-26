
from io import TextIOBase
from pathlib import Path
from tokenize import detect_encoding
from unittest.mock import Mock

import pytest

from isort.io import File, UnsupportedEncoding


def test_none_input():
    # Create a mock for readline that will raise an exception to simulate the error scenario
    mock_readline = Mock(side_effect=Exception("Simulated readline error"))
    
    # Call the detect_encoding function with a non-existent filename to trigger the error handling
    with pytest.raises(UnsupportedEncoding):
        File.detect_encoding("nonexistentfile", mock_readline)
