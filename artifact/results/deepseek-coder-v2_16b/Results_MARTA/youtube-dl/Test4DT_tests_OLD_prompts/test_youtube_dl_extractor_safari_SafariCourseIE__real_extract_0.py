
import pytest
from unittest.mock import patch
from youtube_dl.extractor.safari import SafariCourseIE
from youtube_dl.compat import compat_str
from youtube_dl.utils import ExtractorError

# Test 1: Extract information from a valid course URL on safaribooksonline.com

# Test 2: Handle URLs that are not valid course pages (should raise ExtractorError)
def test_real_extract_invalid_course():
    url = 'https://www.safaribooksonline.com/videos/python-programming-language/9780134217314'
    with patch('youtube_dl.extractor.safari.SafariCourseIE._download_json', return_value={}):
        safari_course = SafariCourseIE()
        with pytest.raises(ExtractorError):
            safari_course._real_extract(url)

# Test 3: Extract information from a course URL on Oreilly's website

# Test 4: Extract information from an API URL