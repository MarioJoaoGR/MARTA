
from isort.deprecated.finders import ReqsBaseFinder
import pytest
from unittest.mock import patch

@pytest.fixture
def base_finder():
    return ReqsBaseFinder(config=None, path=".")

def test_normalize_name_happy_path(base_finder):
    with patch.object(ReqsBaseFinder, '_load_mapping', return_value={'Django': 'django'}):
        assert base_finder._normalize_name('Django') == 'django'
        assert base_finder._normalize_name('django-haystack') == 'django_haystack'
        assert base_finder._normalize_name('Flask-RESTFul') == 'flask_restful'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input_happy_path
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_valid_input_happy_path.py:8:11: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""