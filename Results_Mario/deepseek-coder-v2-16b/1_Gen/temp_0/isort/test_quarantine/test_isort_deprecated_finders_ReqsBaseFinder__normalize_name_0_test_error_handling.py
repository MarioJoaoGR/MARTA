
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from configparser import Config

@pytest.fixture
def finder():
    return ReqsBaseFinder(config=Config(), path=".")

def test_normalize_name(finder):
    assert finder._normalize_name("Django") == "django"
    assert finder._normalize_name("django-haystack") == "django_haystack"
    assert finder._normalize_name("Flask-RESTFul") == "flask_restful"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_error_handling
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_error_handling.py:4:0: E0611: No name 'Config' in module 'configparser' (no-name-in-module)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_error_handling.py:8:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""