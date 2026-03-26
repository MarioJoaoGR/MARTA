
import io
from pathlib import Path
from unittest.mock import patch, mock_open
import pytest
from flutes.io import reverse_open

def test_reverse_open_error_case():
    with pytest.raises(ValueError):
        with patch("builtins.open", mock_open()) as mocked_open:
            with patch("flutes.io._ReverseReadlineFile.MAX_CHAR_BYTES", 1024):
                reverse_open("test_file.txt", buffer_size=512)
