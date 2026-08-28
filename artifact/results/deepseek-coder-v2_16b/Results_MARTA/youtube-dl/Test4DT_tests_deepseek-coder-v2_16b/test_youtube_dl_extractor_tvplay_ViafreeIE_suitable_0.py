
import pytest
from youtube_dl.extractor import ViafreeIE

# Test to check if a valid URL is suitable for extraction
def test_suitable():
    url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
    assert ViafreeIE.suitable(url) == True, "Expected the URL to be suitable for extraction"

# Test to extract information from a valid URL

# Test to check if a URL is not suitable for extraction when it should be false
def test_not_suitable():
    url = 'http://www.example.com'
    assert ViafreeIE.suitable(url) == False, "Expected the URL to be unsuitable for extraction"