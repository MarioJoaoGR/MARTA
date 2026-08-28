
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.nrk import NRKIE


def test_invalid_url():
    nrk_ie = NRKIE()
    url = 'http://www.example.com/video/invalid'
    with pytest.raises(Exception):
        nrk_ie._real_extract(url)

def test_no_formats_found():
    with patch('youtube_dl.extractor.nrk.NRKIE._call_api', return_value={'playable': {'assets': []}}):
        nrk_ie = NRKIE()
        url = 'http://www.nrk.no/video/PS*150533'
        with pytest.raises(Exception) as e:
            nrk_ie._real_extract(url)
        assert str(e.value) == "No video formats found; please report this issue on https://yt-dl.org/bug . Make sure you are using the latest version; see  https://yt-dl.org/update  on how to update. Be sure to call youtube-dl with the --verbose flag and include its complete output."