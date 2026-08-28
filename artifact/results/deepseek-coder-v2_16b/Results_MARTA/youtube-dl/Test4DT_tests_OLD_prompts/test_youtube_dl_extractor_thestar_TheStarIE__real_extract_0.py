
import pytest
from unittest.mock import patch
from youtube_dl.extractor.thestar import TheStarIE

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup code here if needed
    pass


def test_invalid_url():
    extractor = TheStarIE()
    with patch('youtube_dl.extractor.thestar.TheStarIE._download_webpage', return_value='mocked webpage'):
        with pytest.raises(Exception):
            info_dict = extractor._real_extract('http://www.invalidurl.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html')