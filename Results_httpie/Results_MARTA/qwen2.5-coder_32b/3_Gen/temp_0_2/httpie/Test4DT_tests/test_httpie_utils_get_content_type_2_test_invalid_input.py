
import mimetypes
from unittest.mock import patch

def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate
    for Content-Type headers, or ``None`` if the file type is unknown
    to ``mimetypes``.
    """
    guessed_type = mimetypes.guess_type(filename, strict=False)
    return guessed_type[0] if guessed_type else None

def test_invalid_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = None
        filename = "nonexistentfile.txt"
    
        # Call the function and assert that it returns None for an invalid file path
        result = get_content_type(filename)
        assert result is None
