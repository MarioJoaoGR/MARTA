
import pytest
from unittest.mock import patch
import mimetypes

def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate for Content-Type headers, or ``None`` if the file type is unknown to ``mimetypes``.
    """
    return mimetypes.guess_type(filename, strict=False)[0]

@pytest.mark.parametrize("filename, expected", [
    ("example.txt", "text/plain"),
    ("report.pdf", "application/pdf"),
    ("unknownfile.xyz", None),
])
def test_valid_input(filename, expected):
    with patch('mimetypes.guess_type') as mock_guess_type:
        # Mock the return value of guess_type based on the filename
        if expected is not None:
            mock_guess_type.return_value = (expected, None)
        else:
            mock_guess_type.return_value = (None, None)
        
        assert get_content_type(filename) == expected
