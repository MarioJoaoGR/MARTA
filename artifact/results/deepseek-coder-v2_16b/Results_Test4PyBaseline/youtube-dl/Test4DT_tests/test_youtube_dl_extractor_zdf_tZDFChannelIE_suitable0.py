
import pytest
from youtube_dl.extractor import ZDFChannelIE

# Initialize the ZDFChannelIE class
zdf_ie = ZDFChannelIE()

# Test cases for checking if a URL is suitable
def test_suitable_valid_url():
    url = 'https://www.zdf.de/sport/das-aktuelle-sportstudio'
    assert zdf_ie.suitable(url) == True, "Expected the valid URL to be suitable"

def test_suitable_invalid_url():
    url = 'https://www.example.com'