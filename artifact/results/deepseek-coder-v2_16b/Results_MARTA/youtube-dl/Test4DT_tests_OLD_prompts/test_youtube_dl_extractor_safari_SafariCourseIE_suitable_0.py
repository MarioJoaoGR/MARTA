
import pytest
from unittest.mock import patch
from youtube_dl.extractor.safari import SafariCourseIE

def test_suitable_for_safaribooksonline():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._VALID_URL', new='https://www.safaribooksonline.com/library/view/.+/9780133392838/'):
        assert SafariCourseIE.suitable('https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/') == True

def test_not_suitable_for_oreilly():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._VALID_URL', new='https://www.safaribooksonline.com/library/view/.+/9780133392838/'):
        assert SafariCourseIE.suitable('https://www.oreilly.com/api/v1/book/9781449396459/?override_format=json') == False

def test_not_suitable_for_techbus():
    with patch('youtube_dl.extractor.safari.SafariCourseIE._VALID_URL', new='https://www.safaribooksonline.com/library/view/.+/9780133392838/'):
        assert SafariCourseIE.suitable('http://techbus.safaribooksonline.com/9780134426365') == False
