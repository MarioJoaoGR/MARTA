
import mimetypes
from unittest.mock import patch

def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate
    for Content-Type headers, or ``None`` if the file type is unknown
    to ``mimetypes``.
    """
    if filename is None:
        return None
    guessed_type = mimetypes.guess_type(filename, strict=False)
    if guessed_type[0] is not None:
        return guessed_type[0]
    else:
        return None

def test_none_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = None
        assert get_content_type(None) is None
