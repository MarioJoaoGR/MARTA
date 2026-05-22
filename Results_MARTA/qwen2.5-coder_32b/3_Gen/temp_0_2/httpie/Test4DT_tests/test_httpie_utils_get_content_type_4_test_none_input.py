
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

# Test case for get_content_type with a filename that does not have an extension
def test_none_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = None
        
        result = get_content_type("nonexistentfile")
        assert result is None, f"Expected None for filename without extension, but got {result}"
