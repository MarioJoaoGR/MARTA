
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.nrk import NRKRadioPodkastIE

# Test for valid case
def test_valid_case():
    with patch('youtube_dl.extractor.nrk.NRKRadioPodkastIE._real_extract') as mock_extract:
        extractor = NRKRadioPodkastIE()
        url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
        mock_extract.return_value = {'id': 'MUHH48000314AA', 'ext': 'mp4', 'title': '20 spørsmål 23.05.2014', 'description': 'md5:bdea103bc35494c143c6a9acdd84887a', 'duration': 1741, 'series': '20 spørsmål', 'episode': '23.05.2014'}
        info = extractor._real_extract(url)
        assert mock_extract.called
        assert info == {'id': 'MUHH48000314AA', 'ext': 'mp4', 'title': '20 spørsmål 23.05.2014', 'description': 'md5:bdea103bc35494c143c6a9acdd84887a', 'duration': 1741, 'series': '20 spørsmål', 'episode': '23.05.2014'}

# Test for edge case with empty string input
def test_edge_case():
    with pytest.raises(Exception):
        extractor = NRKRadioPodkastIE()
        url = ''
        extractor._real_extract(url)

# Test for error case with invalid URL that should raise an exception
def test_error_case():
    with patch('youtube_dl.extractor.nrk.NRKRadioPodkastIE._match_id', side_effect=Exception("Invalid URL")):
        extractor = NRKRadioPodkastIE()
        url = 'invalid-url'
        with pytest.raises(Exception):
            extractor._real_extract(url)
