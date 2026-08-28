
import pytest
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

@pytest.fixture
def instance():
    return NRKTVSerieBaseIE()

# Test scenario 1: Valid input with 'episodes' key present
def test_valid_input_episodes(instance):
    embedded = {'episodes': [{"prfId": "12345"}]}
    result = instance._extract_assets_key(embedded)
    assert result == 'episodes'

# Test scenario 2: Valid input with 'instalments' key present
def test_valid_input_instalments(instance):
    embedded = {'instalments': [{"prfId": "12345"}]}
    result = instance._extract_assets_key(embedded)
    assert result == 'instalments'

# Test scenario 3: Invalid input with neither 'episodes' nor 'instalments' key present
def test_invalid_input(instance):
    embedded = {'other': [{"prfId": "12345"}]}
    result = instance._extract_assets_key(embedded)
    assert result is None
