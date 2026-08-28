
import pytest
from youtube_dl.extractor.heise import HeiseIE

# Test for valid case where URL contains a video

# Test for case where URL does not contain a video (should return None or raise an exception)
def test_invalid_case():
    heise_extractor = HeiseIE()
    url = 'http://www.heise.de/non-video-page'
    
    with pytest.raises(Exception):
        info_dict = heise_extractor._real_extract(url)