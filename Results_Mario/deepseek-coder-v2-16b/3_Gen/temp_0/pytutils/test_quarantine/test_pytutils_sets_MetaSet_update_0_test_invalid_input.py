
import pytest
from pytutils.sets import MetaSet
from unittest.mock import MagicMock, patch

def consume(iterable):
    for _ in iterable:
        pass

@pytest.fixture
def meta_set():
    return MetaSet()

def test_update_with_valid_iterable(meta_set):
    lst = [1, 2, 3, 4]
    with patch('pytutils.sets.consume') as mock_consume:
        meta_set.update(lst)
        assert len(meta_set._store) == len(lst)
        for item in lst:
            assert item in meta_set._store
        mock_consume.assert_called_once_with(map(meta_set.add, lst))

def test_update_with_invalid_iterable(meta_set):
    invalid_iterable = None  # This should be an iterable that does not support iteration
    with pytest.raises(TypeError) as excinfo:
        meta_set.update(invalid_iterable)
    assert "argument" in str(excinfo.value) and "iterable" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""