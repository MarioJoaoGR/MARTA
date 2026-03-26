
from isort.deprecated.finders import ReqsBaseFinder

class TestReqsBaseFinder:
    def test_edge_case_none(self):
        finder = ReqsBaseFinder(config=None, path=".")
        assert finder._normalize_name("Django") == "django"
        assert finder._normalize_name("django-haystack") == "django_haystack"
        assert finder._normalize_name("Flask-RESTFul") == "flask_restful"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_edge_case_none
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__normalize_name_0_test_edge_case_none.py:6:17: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""