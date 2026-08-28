
import pytest
from youtube_dl.extractor.soundgasm import SoundgasmIE

# Test for valid URL extraction

# Test for invalid URL (should raise an exception)
def test_invalid_url():
    extractor = SoundgasmIE()
    url = 'http://example.com/invalid-soundgasm-url'
    
    with pytest.raises(Exception):
        info_dict = extractor._real_extract(url)