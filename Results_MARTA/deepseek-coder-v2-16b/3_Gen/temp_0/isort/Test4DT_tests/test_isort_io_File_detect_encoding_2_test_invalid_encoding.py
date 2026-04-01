
from io import BytesIO, TextIOBase
from pathlib import Path
from tokenize import detect_encoding
from unittest.mock import Mock

import pytest

from isort.exceptions import UnsupportedEncoding
# Assuming the File class and its methods are defined in a module named 'isort.io'
from isort.io import File


def test_invalid_encoding():
    # Create a mock for readline that raises an exception when called
    mock_readline = Mock(side_effect=ValueError("Mocked ValueError"))
    
    with pytest.raises(UnsupportedEncoding):
        # Attempt to detect encoding, which should raise an UnsupportedEncoding error
        File.detect_encoding("mock_file", mock_readline)
