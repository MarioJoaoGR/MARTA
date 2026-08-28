
import pytest
from youtube_dl.extractor import NRKTVSeasonIE

# Test valid TV season URL
def test_valid_case_1():
    url = 'https://tv.nrk.no/serie/backstage/sesong/1'
    assert NRKTVSeasonIE().suitable(url) is True

# Test valid radio podcast season URL
def test_valid_case_2():
    url = 'https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant'
    assert NRKTVSeasonIE().suitable(url) is True

# Test invalid URL
def test_invalid_case():
    url = 'https://www.example.com/invalid-url'
    assert NRKTVSeasonIE().suitable(url) is False
