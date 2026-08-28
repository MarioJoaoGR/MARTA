
import pytest
from youtube_dl.extractor.safari import SafariCourseIE

# Test for a valid URL
def test_valid_case():
    url = 'https://www.safaribooksonline.com/library/view/hadoop-fundamentals-livelessons/9780133392838/'
    assert SafariCourseIE.suitable(url) == True, "Expected True for a valid URL"

# Test with None input to check error handling
def test_edge_case():
    url = None
    with pytest.raises(TypeError):
        SafariCourseIE.suitable(url)

# Test with an invalid URL that should return False
def test_invalid_input():
    url = 'https://www.example.com/invalid-url'
    assert SafariCourseIE.suitable(url) == False, "Expected False for an invalid URL"
