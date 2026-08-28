
import pytest
from unittest.mock import patch
from youtube_dl.extractor.heise import HeiseIE



def test_invalid_url():
    heise_extractor = HeiseIE()
    with pytest.raises(Exception):
        heise_extractor._real_extract('http://www.heise.de/invalid-url')