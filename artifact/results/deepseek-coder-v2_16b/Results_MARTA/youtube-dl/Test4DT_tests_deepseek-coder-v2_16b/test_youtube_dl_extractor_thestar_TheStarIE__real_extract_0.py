
import pytest
from youtube_dl.extractor.thestar import TheStarIE


def test_invalid_input():
    extractor = TheStarIE()
    url = "http://www.thestar.com/invalid-url"
    with pytest.raises(Exception):
        info_dict = extractor._real_extract(url)