
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE
import pytest

# Test for extracting entries when given a valid list of episodes

# Test for handling invalid entries in the list

# Test for handling non-list input
def test_NRKTVSerieBaseIE__extract_entries_non_list():
    nrk_extractor = NRKTVSerieBaseIE()
    non_list = {'prfId': '12345'}  # This is not a list, but a single dictionary
    extracted_info = nrk_extractor._extract_entries(non_list)
    
    assert isinstance(extracted_info, list), "Expected an empty list for non-list input"
    assert len(extracted_info) == 0, "Expected no entries for non-list input"