
import pytest
from isort.deprecated.finders import ReqsBaseFinder

# Assuming Config and other necessary imports are available in this scope
@pytest.fixture(scope="module")
def base_finder():
    return ReqsBaseFinder(config=Config(), path=".")

def test_normalize_name_valid_input(base_finder):
    # Test with a valid package name without hyphens
    assert base_finder._normalize_name("Django") == "django"
    
    # Test with a valid package name containing hyphens
    assert base_finder._normalize_name("django-haystack") == "django_haystack"
    
    # Test with a valid package name containing multiple hyphens
    assert base_finder._normalize_name("Flask-RESTFul") == "flask_restful"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input.py:8:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input.py:8:33: E0602: Undefined variable 'Config' (undefined-variable)


"""