
import pytest
from youtube_dl.extractor.zdf import ZDFChannelIE

# Test case for checking if a URL is suitable when it matches the valid pattern
def test_suitable_when_url_matches():
    zdf_ie = ZDFChannelIE()
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    assert zdf_ie.suitable(url) is True, "Expected suitable to be True for a valid URL"

# Test case for checking if a URL is not suitable when it does not match the valid pattern
def test_not_suitable_when_url_does_not_match():
    zdf_ie = ZDFChannelIE()
    url = 'https://www.example.com/invalid-path'
    assert zdf_ie.suitable(url) is False, "Expected suitable to be False for an invalid URL"

# Test case for checking if a None URL results in not suitable