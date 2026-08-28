
import re
from youtube_dl.extractor import NRKSkoleIE
import pytest

# Initialize the class for testing
@pytest.fixture(scope="module")
def nrk_extractor():
    return NRKSkoleIE()

# Test cases for valid URLs
@pytest.mark.parametrize("url, expected", [
    ('https://www.nrk.no/skole/?mediaId=14099', '14099'),
    ('https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355', '19355')
])
def test_valid_urls(nrk_extractor, url, expected):
    match = re.match(nrk_extractor._VALID_URL, url)
    assert match is not None, f"No match found for {url}"
    assert match.group('id') == expected, f"Expected ID {expected} but got {match.group('id')}"

# Test case for invalid URL
def test_invalid_url(nrk_extractor):
    invalid_url = 'https://www.example.com/invalid-page'
    match = re.match(nrk_extractor._VALID_URL, invalid_url)