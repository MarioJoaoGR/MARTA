
import pytest
from youtube_dl.extractor.nrk import NRKPlaylistIE

# Test for valid input URL

# Test for edge case URL

# Test for invalid input URL
def test_invalid_input():
    nrk_playlist = NRKPlaylistIE()
    url = 'http://www.example.com/non-existing-page'
    with pytest.raises(AttributeError):
        nrk_playlist.extract_info(url)