
import pytest
import mimetypes
from unittest.mock import patch

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

# Test cases for get_content_type function

@pytest.fixture(params=['example.txt', 'report.pdf', 'unknownfile'])
def filename(request):
    return request.param

def test_valid_input_txt(filename):
    if filename == 'example.txt':
        assert get_content_type('example.txt') == 'text/plain'
    elif filename == 'report.pdf':
        assert get_content_type('report.pdf') == 'application/pdf'

def test_valid_input_pdf(filename):
    if filename == 'report.pdf':
        assert get_content_type('report.pdf') == 'application/pdf'

def test_invalid_input(filename):
    if filename == 'unknownfile':
        assert get_content_type('unknownfile') is None
