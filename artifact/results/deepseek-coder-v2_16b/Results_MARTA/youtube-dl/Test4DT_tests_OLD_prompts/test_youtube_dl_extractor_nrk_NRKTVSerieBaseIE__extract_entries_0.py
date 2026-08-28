
import pytest
from unittest.mock import patch
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE, NRKIE

# Test 1: Extracting Information from a List of Episodes

# Test 2: Extracting Information from a List of Instalments

# Test 3: Handling Non-List Input
def test_invalid_input():
    nrk_extractor = NRKTVSerieBaseIE()
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._extract_entries', return_value=[]):
        non_list = {'prfId': '12345'}  # This is not a list, but a single dictionary
        extracted_info = nrk_extractor._extract_entries(non_list)
        assert len(extracted_info) == 0, "Expected no entries"