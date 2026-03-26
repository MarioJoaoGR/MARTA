
import pytest
from urllib.parse import urlparse

def _extract_google_drive_file_id(url: str) -> str:
    parsed_url = urlparse(url)
    path = parsed_url.path
    if '/d/' in path:
        return path.split('/d/')[1].split('/')[0]
    else:
        return ''

def test_invalid_input():
    url = 'https://example.com/wrong/url'
    assert _extract_google_drive_file_id(url) == '', f"Expected empty string for invalid URL, but got {_extract_google_drive_file_id(url)}"
