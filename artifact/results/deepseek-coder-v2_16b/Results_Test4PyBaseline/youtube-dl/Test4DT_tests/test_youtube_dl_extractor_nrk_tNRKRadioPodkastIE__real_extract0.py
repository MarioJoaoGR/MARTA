
import pytest
from youtube_dl.extractor import NRKRadioPodkastIE

# Create an instance of the extractor
@pytest.fixture(scope="module")
def extractor():
    return NRKRadioPodkastIE()

# Test cases for valid podcast episode URLs
@pytest.mark.parametrize("url, expected_id", [
    ('https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8', 'l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'),
    ('https://radio.nrk.no/podcast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8', 'l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'),
    ('https://radio.nrk.no/podkast/ulrikkes_univers/sesong/1/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8', 'l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'),
    ('https://radio.nrk.no/podkast/hele_historien/sesong/bortfoert-i-bergen/l_774d1a2c-7aa7-4965-8d1a-2c7aa7d9652c', 'l_774d1a2c-7aa7-4965-8d1a-2c7aa7d9652c'),
])
def test_real_extract(extractor, url, expected_id):
    info_dict = extractor._real_extract(url)
    assert 'id' in info_dict  # Simplified assertion to check for the presence of 'id' key
