
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

# Test Scenario 1: test_valid_case
def test_valid_case():
    nrk_extractor = NRKTVSerieBaseIE()
    data = {'_embedded': {'episodes': [{'prfId': '12345'}, {'episodeId': '67890'}]}}
    display_id = 'series123'
    
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._entries', return_value=iter([{'url': 'https://example.com/video1', 'ie_key': 'NRKIE', 'video_id': '12345'}, {'url': 'https://example.com/video2', 'ie_key': 'NRKIE', 'video_id': '67890'}])):
        extracted_info = list(nrk_extractor._entries(data, display_id))
    
    assert len(extracted_info) == 2
    for info in extracted_info:
        assert 'url' in info
        assert 'ie_key' in info
        assert 'video_id' in info

# Test Scenario 2: test_edge_case
def test_edge_case():
    nrk_extractor = NRKTVSerieBaseIE()
    data = None
    display_id = 'series123'
    
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._entries', return_value=iter([])):
        extracted_info = list(nrk_extractor._entries(data, display_id))
    
    assert len(extracted_info) == 0

# Test Scenario 3: test_invalid_input
def test_invalid_input():
    nrk_extractor = NRKTVSerieBaseIE()
    data = {'invalid': 'data'}
    display_id = 'series123'
    
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._entries', return_value=iter([])):
        extracted_info = list(nrk_extractor._entries(data, display_id))
    
    assert len(extracted_info) == 0
