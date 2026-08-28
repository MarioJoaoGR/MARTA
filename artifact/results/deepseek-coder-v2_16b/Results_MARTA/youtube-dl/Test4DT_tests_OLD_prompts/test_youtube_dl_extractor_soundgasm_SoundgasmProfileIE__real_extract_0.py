
import pytest
from unittest.mock import patch
from youtube_dl.extractor.soundgasm import SoundgasmProfileIE

@pytest.fixture
def extractor():
    return SoundgasmProfileIE()


def test_invalid_url(extractor):
    with patch('youtube_dl.extractor.soundgasm.SoundgasmProfileIE._download_webpage', return_value='<html>some content</html>'):
        with pytest.raises(Exception):
            extractor._real_extract('http://invalidurl.com')