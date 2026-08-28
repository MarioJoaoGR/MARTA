
import pytest
from unittest.mock import patch
from youtube_dl.extractor.soundgasm import SoundgasmIE

# Test for valid case with mocked webpage content
@pytest.fixture(autouse=True)
def setup():
    extractor = SoundgasmIE()
    with patch('youtube_dl.extractor.soundgasm.SoundgasmIE._download_webpage', return_value='mocked_webpage'):
        yield extractor


# Test for invalid URL case
def test_invalid_url():
    extractor = SoundgasmIE()
    url = 'http://example.com/invalid-soundgasm-url'
    with pytest.raises(Exception):
        info_dict = extractor._real_extract(url)