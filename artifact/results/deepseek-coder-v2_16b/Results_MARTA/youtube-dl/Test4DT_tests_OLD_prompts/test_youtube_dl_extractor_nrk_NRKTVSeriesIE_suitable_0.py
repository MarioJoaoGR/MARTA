
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor import NRKTVSeriesIE

# Test valid case 1: Test standard input for a valid NRK TV series URL
def test_valid_case_1():
    with patch('youtube_dl.extractor.NRKTVSeriesIE._real_extract', return_value={'id': 'groenn-glede', 'title': 'Grønn glede', 'description': 'md5:7576e92ae7f65da6993cf90ee29e4608'}):
        assert NRKTVSeriesIE().suitable('https://tv.nrk.no/serie/groenn-glede') is True

# Test valid case 2: Test standard input for a valid NRK podcast URL
def test_valid_case_2():
    with patch('youtube_dl.extractor.NRKTVSeriesIE._real_extract', return_value={'id': 'ulrikkes_univers'}):
        assert NRKTVSeriesIE().suitable('https://radio.nrk.no/podkast/ulrikkes_univers') is True

# Test invalid case: Test for an invalid URL that should return False
def test_invalid_case():
    with patch('youtube_dl.extractor.NRKTVSeriesIE._real_extract', side_effect=Exception):
        assert NRKTVSeriesIE().suitable('http://example.com/invalid-url') is False
