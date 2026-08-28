
import pytest
from youtube_dl.extractor import SafariCourseIE
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError
from youtube_dl.utils import ExtractorError  # Importing ExtractorError correctly

# Fixture to create an instance of SafariCourseIE for testing
@pytest.fixture
def safari_course_ie():
    return SafariCourseIE()

# Test cases for _real_extract method
class TestSafariCourseIE:
    
    @patch('youtube_dl.extractor.SafariCourseIE._download_json')
    def test_no_chapters(self, mock_download_json, safari_course_ie):
        # Mock data to simulate a failed download of course JSON
        mock_download_json.return_value = {}  # Empty dictionary indicating no chapters found
        
        url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
        with pytest.raises(ExtractorError) as exc_info:
            safari_course_ie._real_extract(url)
        
        assert str(exc_info.value).startswith('No chapters found for course')  # Ensure the error message is correct
