
import pytest
from youtube_dl.extractor import SafariCourseIE
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError  # Assuming ExtractorError is replaced by HTTPError for demonstration purposes

# Fixture to create an instance of SafariCourseIE for testing
@pytest.fixture
def safari_course_ie():
    return SafariCourseIE()

# Test cases for _real_extract method
class TestSafariCourseIE:
    
    @patch('youtube_dl.extractor.SafariCourseIE._download_json')
    def test_valid_url(self, mock_download_json, safari_course_ie):
        # Mock data to simulate a successful download of course JSON
        mock_download_json.return_value = {
            'title': 'Hadoop Fundamentals LiveLessons',
            'chapters': ['chapter1', 'chapter2']
        }
        
        url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
        result = safari_course_ie._real_extract(url)
        
        assert isinstance(result, dict)
        assert 'id' in result
        assert 'title' in result
        assert 'entries' in result