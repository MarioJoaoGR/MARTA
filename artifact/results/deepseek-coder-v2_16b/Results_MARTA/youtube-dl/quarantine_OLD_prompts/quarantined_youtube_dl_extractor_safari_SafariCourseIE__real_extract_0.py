
import pytest
from unittest.mock import patch
from youtube_dl.extractor.safari import SafariCourseIE
from youtube_dl.compat import compat_str
from youtube_dl.utils import ExtractorError

# Test 1: Extracting information from a valid course URL
def test_real_extract_valid_course():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._download_json', return_value={'chapters': ['chapter1', 'chapter2'], 'title': 'Valid Course Title'})):
        safari_course = SafariCourseIE()
        url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
        info_dict = safari_course._real_extract(url)
        assert info_dict['id'] == '9780133392838'
        assert info_dict['title'] == 'Valid Course Title'
        assert len(info_dict['chapters']) == 2

# Test 2: Handling URLs with specific domains and paths
def test_real_extract_specific_domain():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._download_json', return_value={'chapters': ['chapter1', 'chapter2'], 'title': 'Valid Course Title'})):
        safari_course = SafariCourseIE()
        url = 'https://www.oreilly.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
        info_dict = safari_course._real_extract(url)
        assert info_dict['id'] == '9780133392838'
        assert info_dict['title'] == 'Valid Course Title'
        assert len(info_dict['chapters']) == 2

# Test 3: Handling API URLs
def test_real_extract_api_url():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._download_json', return_value={'chapters': ['chapter1', 'chapter2'], 'title': 'Valid Course Title'})):
        safari_course = SafariCourseIE()
        url = 'https://www.safaribooksonline.com/api/v1/book/9781449396459/?override_format=json'
        info_dict = safari_course._real_extract(url)
        assert info_dict['id'] == '9781449396459'
        assert info_dict['title'] == 'Valid Course Title'
        assert len(info_dict['chapters']) == 2

# Test 4: Handling URLs with no chapters found
def test_real_extract_no_chapters():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._download_json', return_value={}):
        safari_course = SafariCourseIE()
        url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
        with pytest.raises(ExtractorError) as excinfo:
            safari_course._real_extract(url)
        assert 'No chapters found' in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: unmatched ')' (line 10, col 160)
    with patch('youtube_dl.extractor.safari.SafariCourseIE._download_json', return_value={'chapters': ['chapter1', 'chapter2'], 'title': 'Valid Course Title'})):
"""