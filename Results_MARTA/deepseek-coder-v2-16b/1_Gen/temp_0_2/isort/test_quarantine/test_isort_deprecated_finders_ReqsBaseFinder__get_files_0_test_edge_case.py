
import pytest
from unittest.mock import MagicMock
from isort.deprecated.finders import ReqsBaseFinder
from config import Config

@pytest.fixture
def setup_finder():
    config = Config()
    finder = ReqsBaseFinder(config=config, path=".")
    return finder

def test_init(setup_finder):
    finder = setup_finder
    assert finder.enabled is False
    assert finder.path == "."
    assert isinstance(finder.config, Config)
    assert finder.mapping == {}
    assert finder.names == []

def test_get_files(setup_finder):
    # Mocking _get_parents and _get_files_from_dir methods
    setup_finder._get_parents = MagicMock(return_value=["mocked_path1", "mocked_path2"])
    setup_finder._get_files_from_dir = MagicMock(side_effect=[["file1.txt", "file2.txt"], ["file3.txt"]])
    
    files = list(setup_finder._get_files())
    assert len(files) == 3
    assert "mocked_path1/file1.txt" in files
    assert "mocked_path1/file2.txt" in files
    assert "mocked_path2/file3.txt" in files

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_files_0_test_edge_case
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_0_test_edge_case.py:5:0: E0401: Unable to import 'config' (import-error)
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_files_0_test_edge_case.py:10:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""