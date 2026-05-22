
import pytest
from unittest.mock import patch
import mimetypes

def get_content_type(filename):
    """Return the content type for ``filename`` in format appropriate for Content-Type headers, or ``None`` if the file type is unknown to ``mimetypes``."""
    return mimetypes.guess_type(filename, strict=False)[0]

@pytest.mark.parametrize("filename, expected", [
    ("example.txt", "text/plain"),
    ("report.pdf", "application/pdf"),
    ("unknownfile.xyz", None),
])
def test_valid_input(filename, expected):
    with patch('mimetypes.guess_type') as mock_guess_type:
        # Set up the mock to return the expected content type based on the filename
        if expected is not None:
            mock_guess_type.return_value = (expected, None)  # Return tuple (content_type, encoding)
        else:
            mock_guess_type.return_value = (None, None)
        
        # Call the function under test
        result = get_content_type(filename)
        
        # Assert that the mock was called with the correct filename
        mock_guess_type.assert_called_once_with(filename, strict=False)
        
        # Assert the expected outcome based on the mocked behavior
        assert result == expected
