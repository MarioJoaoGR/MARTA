
import pytest
from httpie.utils import get_content_type

def test_get_content_type_known_extension():
    assert get_content_type('example.txt') == 'text/plain'
    assert get_content_type('report.pdf') == 'application/pdf'
    assert get_content_type('image.jpg') == 'image/jpeg'
