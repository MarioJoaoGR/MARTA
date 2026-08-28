
import pytest
from youtube_dl.extractor import NRKTVSeriesIE

# Test valid NRK TV series URL
def test_valid_case_1():
    instance = NRKTVSeriesIE()
    url = 'https://tv.nrk.no/serie/groenn-glede'
    assert instance.suitable(url) is True

# Test valid NRK podcast URL
def test_valid_case_2():
    instance = NRKTVSeriesIE()
    url = 'https://radio.nrk.no/podkast/ulrikkes_univers'
    assert instance.suitable(url) is True

# Test invalid URL
def test_invalid_case():
    instance = NRKTVSeriesIE()
    url = 'http://example.com/invalid-url'
    assert instance.suitable(url) is False
