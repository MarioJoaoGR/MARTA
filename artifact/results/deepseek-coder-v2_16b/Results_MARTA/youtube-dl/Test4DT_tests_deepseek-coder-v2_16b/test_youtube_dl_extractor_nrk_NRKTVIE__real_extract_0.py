
import pytest
from youtube_dl.extractor.nrk import NRKIE

# Test for valid case scenario

# Test for edge case scenario where URL is empty
def test_edge_case():
    nrk_ie = NRKIE()
    url = ''
    with pytest.raises(Exception):
        nrk_ie._real_extract(url)

# Test for invalid input scenario
def test_invalid_input():
    nrk_ie = NRKIE()
    url = 'https://example.com/invalid'
    with pytest.raises(Exception):
        nrk_ie._real_extract(url)