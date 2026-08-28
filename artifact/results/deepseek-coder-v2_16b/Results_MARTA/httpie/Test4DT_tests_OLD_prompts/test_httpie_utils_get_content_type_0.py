
import pytest
from unittest.mock import patch
import mimetypes

def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate
    for Content-Type headers, or ``None`` if the file type is unknown
    to ``mimetypes``.
    """
    mime, encoding = mimetypes.guess_type(filename, strict=False)
    if mime:
        content_type = mime
        if encoding:
            content_type = '%s; charset=%s' % (mime, encoding)
        return content_type

# Test scenarios
def test_valid_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = ('text/plain', None)
        assert get_content_type('example.txt') == 'text/plain'
        
        mock_guess_type.return_value = ('application/pdf', None)
        assert get_content_type('report.pdf') == 'application/pdf'
        
        mock_guess_type.return_value = ('image/jpeg', None)
        assert get_content_type('image.jpg') == 'image/jpeg'

def test_none_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = (None, None)
        assert get_content_type(None) is None

def test_invalid_input():
    with patch('mimetypes.guess_type') as mock_guess_type:
        mock_guess_type.return_value = (None, None)
        assert get_content_type('unknownfile.xyz') is None
