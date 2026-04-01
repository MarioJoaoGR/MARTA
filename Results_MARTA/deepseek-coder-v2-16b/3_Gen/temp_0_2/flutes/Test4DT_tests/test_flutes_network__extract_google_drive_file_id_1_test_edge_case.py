
import pytest
from urllib.parse import urlparse

def _extract_google_drive_file_id(url: str) -> str:
    # The ID is the first segment after `/d/`.
    parsed_url = urlparse(url)
    path = parsed_url.path
    if '/d/' in path:
        return path.split('/d/')[1].split('/')[0]
    else:
        return ''

def test_edge_case():
    url = 'https://example.com/randompath'
    assert _extract_google_drive_file_id(url) == '', f"Expected an empty string for URL without '/d/' segment, but got {_extract_google_drive_file_id(url)}"
