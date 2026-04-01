
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from your_module_name.config import Config  # Replace 'your_module_name' with the actual module name

@pytest.fixture
def setup_finder():
    config = Config()  # Assuming you have a Config class defined in your_module_name.config
    finder = ReqsBaseFinder(config=config, path=".")
    return finder

def test_missing_mapping_file(mocker):
    mocker.patch('isort.deprecated.finders.ReqsBaseFinder._load_mapping', side_effect=NotImplementedError)
    
    finder = setup_finder()
    
    assert not finder.enabled
    assert finder.mapping is None
    assert finder.names == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__load_mapping_0_test_missing_mapping_file
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_mapping_0_test_missing_mapping_file.py:4:0: E0401: Unable to import 'your_module_name.config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__load_mapping_0_test_missing_mapping_file.py:9:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""