
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.nrk import NRKIE

# Test function for valid case scenario
def test_valid_case():
    with patch('youtube_dl.extractor.nrk.NRKIE._real_extract', return_value={'id': 'MDDP12000117'}):
        nrk_ie = NRKIE()
        result = nrk_ie._real_extract('https://tv.nrk.no/program/MDDP12000117')
        assert result['id'] == 'MDDP12000117'

# Test function for edge case scenario with None input
def test_edge_case():
    nrk_ie = NRKIE()
    with pytest.raises(Exception):
        nrk_ie._real_extract(None)

# Test function for invalid input and error handling scenario
def test_invalid_input():
    nrk_ie = NRKIE()
    with pytest.raises(Exception):
        nrk_ie._real_extract('invalid-url')
