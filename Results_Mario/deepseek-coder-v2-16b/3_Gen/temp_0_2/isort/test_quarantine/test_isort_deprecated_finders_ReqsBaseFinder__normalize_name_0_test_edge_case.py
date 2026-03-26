
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("name", ["Django", "django-haystack", "Flask-RESTFul"])
def test_normalize_name(name):
    with patch('isort.deprecated.finders.ReqsBaseFinder._load_mapping', return_value={}):
        finder = ReqsBaseFinder(config=None, path=".")
        assert finder._normalize_name(name) == name.replace("-", "_").lower()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_edge_case.py:9:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""