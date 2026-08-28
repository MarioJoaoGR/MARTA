
import pytest
from youtube_dl.extractor.soundgasm import SoundgasmProfileIE

    
def test_invalid_input():
    extractor = SoundgasmProfileIE()
    url = 'http://invalidurl.com'
    with pytest.raises(Exception):
        info_dict = extractor._real_extract(url)