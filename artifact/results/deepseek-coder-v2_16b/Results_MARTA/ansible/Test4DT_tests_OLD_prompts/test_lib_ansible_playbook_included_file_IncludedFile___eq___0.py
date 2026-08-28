
import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.included_file import IncludedFile

@pytest.fixture
def create_included_file():
    def _create_included_file(filename, args, vars_, task):
        return IncludedFile(filename, args, vars_, task)
    return _create_included_file


def test_eq_with_different_filenames():
    file1 = IncludedFile("example_file1.txt", {"arg1": "value1"}, {"var1": "value1"}, MagicMock())
    file2 = IncludedFile("example_file2.txt", {"arg1": "value1"}, {"var1": "value1"}, MagicMock())
    assert not (file1 == file2)

def test_eq_with_different_args():
    file1 = IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, MagicMock())
    file2 = IncludedFile("example_file.txt", {"arg1": "value2"}, {"var1": "value1"}, MagicMock())
    assert not (file1 == file2)

def test_eq_with_different_vars():
    file1 = IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value1"}, MagicMock())
    file2 = IncludedFile("example_file.txt", {"arg1": "value1"}, {"var1": "value2"}, MagicMock())
    assert not (file1 == file2)

