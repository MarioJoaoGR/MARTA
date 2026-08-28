
import pytest
from youtube_dl.extractor import SoundgasmIE

# Test for valid URL extraction

# Test for invalid URL handling (expected failure)
def test_invalid_url():
    extractor = SoundgasmIE()
    url = 'http://example.com/invalid-soundgasm-url'
    
    with pytest.raises(Exception):
        info_dict = extractor._real_extract(url)