
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.nrk import NRKBaseIE
from urllib.parse import urljoin

# Test 1: Initialize NRKBaseIE class
def test_initialize_NRKBaseIE():
    nrk_ie = NRKBaseIE()
    assert isinstance(nrk_ie, NRKBaseIE)

# Test 2: Call API method with valid path and video ID
@patch('youtube_dl.extractor.nrk.NRKBaseIE._download_json')
def test_call_api_valid(mock_download_json):
    nrk_ie = NRKBaseIE()
    mock_download_json.return_value = {'data': 'some data'}
    
    path = 'video/info'
    video_id = '12345'
    result = nrk_ie._call_api(path, video_id)
    
    assert mock_download_json.called
    assert mock_download_json.call_args[0][0] == urljoin('http://psapi.nrk.no/', path)
    assert mock_download_json.call_args[0][1] == video_id
    assert result == {'data': 'some data'}

# Test 3: Call API method with invalid path and video ID (should raise error)
@patch('youtube_dl.extractor.nrk.NRKBaseIE._download_json')
def test_call_api_invalid(mock_download_json):
    nrk_ie = NRKBaseIE()
    mock_download_json.side_effect = Exception("API call failed")
    
    path = 'invalid/path'
    video_id = '12345'
    
    with pytest.raises(Exception):
        nrk_ie._call_api(path, video_id)

# Test 4: Call API method with fatal=False (should not raise error)
@patch('youtube_dl.extractor.nrk.NRKBaseIE._download_json')
def test_call_api_fatal_false(mock_download_json):
    nrk_ie = NRKBaseIE()
    mock_download_json.return_value = {'data': 'some data'}
    
    path = 'video/info'
    video_id = '12345'
    result = nrk_ie._call_api(path, video_id, fatal=False)
    
    assert mock_download_json.called
    assert result == {'data': 'some data'}
