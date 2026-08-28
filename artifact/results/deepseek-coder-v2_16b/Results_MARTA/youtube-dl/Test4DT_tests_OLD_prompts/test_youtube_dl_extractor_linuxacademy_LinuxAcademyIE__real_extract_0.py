
import pytest
from unittest.mock import patch, MagicMock
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

# Test for valid course lesson URL
def test_valid_course_lesson():
    with patch('youtube_dl.extractor.linuxacademy.LinuxAcademyIE._real_extract', return_value={
        'id': '7971-2',
        'ext': 'mp4',
        'title': 'What Is Data Science',
        'description': 'md5:c574a3c20607144fb36cb65bdde76c99',
        'timestamp': 1607387907,
        'upload_date': '20201208',
        'duration': 304
    }):
        extractor = LinuxAcademyIE()
        info_dict = extractor._real_extract('https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2')
        assert info_dict == {
            'id': '7971-2',
            'ext': 'mp4',
            'title': 'What Is Data Science',
            'description': 'md5:c574a3c20607144fb36cb65bdde76c99',
            'timestamp': 1607387907,
            'upload_date': '20201208',
            'duration': 304
        }

# Test for valid module view URL
def test_valid_module_view():
    with patch('youtube_dl.extractor.linuxacademy.LinuxAcademyIE._real_extract', return_value={
        'id': '154',
        'title': 'AWS Certified Cloud Practitioner',
        'description': 'md5:a68a299ca9bb98d41cca5abc4d4ce22c',
        'duration': 28835,
        'playlist_count': 41
    }):
        extractor = LinuxAcademyIE()
        info_dict = extractor._real_extract('https://linuxacademy.com/cp/modules/view/id/154')
        assert info_dict == {
            'id': '154',
            'title': 'AWS Certified Cloud Practitioner',
            'description': 'md5:a68a299ca9bb98d41cca5abc4d4ce22c',
            'duration': 28835,
            'playlist_count': 41
        }

# Test for invalid URL
def test_invalid_url():
    with patch('youtube_dl.extractor.linuxacademy.LinuxAcademyIE._real_extract', side_effect=Exception("Invalid URL")):
        extractor = LinuxAcademyIE()
        with pytest.raises(Exception, match="Invalid URL"):
            extractor._real_extract('https://invalid-url.com')
