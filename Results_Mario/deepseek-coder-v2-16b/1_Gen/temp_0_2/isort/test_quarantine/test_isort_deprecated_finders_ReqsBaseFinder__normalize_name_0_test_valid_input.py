
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def setup_finder():
    config = MagicMock()
    finder = ReqsBaseFinder(config=config, path=".")
    return finder

def test_normalize_name_valid_input(setup_finder):
    finder = setup_finder
    assert finder._normalize_name("Django") == "django"
    assert finder._normalize_name("django-haystack") == "django_haystack"
    assert finder._normalize_name("Flask-RESTFul") == "flask_restful"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input.py:9:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""