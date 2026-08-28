
import pytest
from unittest.mock import patch
from youtube_dl.extractor.safari import SafariApiIE


def test_invalid_input():
    safari_api = SafariApiIE()
    with patch('youtube_dl.extractor.safari.SafariApiIE._download_json', side_effect=Exception("Invalid URL")):
        with pytest.raises(Exception):
            safari_api._real_extract('https://www.invalidurl.com/api/v1/book/9780133392838/chapter/part00.html')