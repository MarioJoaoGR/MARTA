
from isort.deprecated.finders import ReqsBaseFinder
import pytest

@pytest.fixture
def finder():
    return ReqsBaseFinder(config=None, path=".")

def test_normalize_name_basic(finder):
    assert finder._normalize_name("Django") == "django"

def test_normalize_name_hyphenated(finder):
    assert finder._normalize_name("django-haystack") == "django_haystack"

def test_normalize_name_multiple_hyphens(finder):
    assert finder._normalize_name("Flask-RESTFul") == "flask_restful"

def test_normalize_name_with_mapping(finder):
    finder.mapping = {"Django": "django", "Flask-RESTFul": "flask_restful"}
    assert finder._normalize_name("Django") == "django"
    assert finder._normalize_name("Flask-RESTFul") == "flask_restful"
    assert finder._normalize_name("django-haystack") == "django_haystack"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input.py:7:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""