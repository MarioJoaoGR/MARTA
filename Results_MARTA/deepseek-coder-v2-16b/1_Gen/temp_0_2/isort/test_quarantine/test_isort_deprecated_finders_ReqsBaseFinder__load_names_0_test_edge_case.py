
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from config import Config

# Mocking the abstract methods since we cannot instantiate an abstract class directly in Python
class MockReqsBaseFinder(ReqsBaseFinder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def _get_files(self):
        yield "mocked_file_path"
    
    def _get_names(self, path: str):
        return ["mocked_name"]

def test_edge_case():
    config = Config()
    finder = MockReqsBaseFinder(config=config)
    
    assert finder.enabled is False
    names = list(finder._load_names())
    assert names == ['mocked_name']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_edge_case.py:4:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_names_0_test_edge_case.py:19:13: E0110: Abstract class 'MockReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""