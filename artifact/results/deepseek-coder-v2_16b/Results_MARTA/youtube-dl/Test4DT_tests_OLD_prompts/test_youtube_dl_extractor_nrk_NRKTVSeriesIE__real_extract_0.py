
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.nrk import NRKTVSeriesIE

# Test Scenario 1: Valid Case
def test_valid_case():
    with patch('youtube_dl.extractor.nrk.NRKTVSeriesIE._real_extract', return_value={'info_dict': {'id': 'groenn-glede'}}):
        nrk_series_extractor = NRKTVSeriesIE()
        url = 'https://tv.nrk.no/serie/groenn-glede'
        info = nrk_series_extractor._real_extract(url)
        assert info['info_dict']['id'] == 'groenn-glede'

# Test Scenario 2: Edge Case with None Input
def test_edge_case():
    with patch('youtube_dl.extractor.nrk.NRKTVSeriesIE._real_extract', return_value=None):
        nrk_series_extractor = NRKTVSeriesIE()
        url = None
        info = nrk_series_extractor._real_extract(url)
        assert info is None

# Test Scenario 3: Error Case with Invalid URL Format
def test_error_case():
    with patch('youtube_dl.extractor.nrk.NRKTVSeriesIE._real_extract', side_effect=Exception("Invalid URL")):
        nrk_series_extractor = NRKTVSeriesIE()
        url = 'https://invalid.url'
        with pytest.raises(Exception):
            nrk_series_extractor._real_extract(url)
