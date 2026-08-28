
import pytest
from youtube_dl.extractor.nrk import NRKRadioPodkastIE


def test_invalid_url():
    extractor = NRKRadioPodkastIE()
    url = 'https://example.com/invalid-podcast'
    with pytest.raises(Exception):
        info = extractor._real_extract(url)