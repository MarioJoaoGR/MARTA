
import pytest
import os
from ansible.plugins.action.copy import _walk_dirs

def test__walk_dirs_basic():
    with pytest.raises(FileNotFoundError):
        result = _walk_dirs('/path/to/source')

def test__walk_dirs_with_base_path():
    with pytest.raises(FileNotFoundError):
        result = _walk_dirs('/path/to/source', base_path='/initial')

def test__walk_dirs_without_local_follow():
    with pytest.raises(FileNotFoundError):
        result = _walk_dirs('/path/to/source', local_follow=False)

def test__walk_dirs_with_trailing_slash_detector():
    def is_remote_slash_significant(path):
        return path.endswith('/')
    with pytest.raises(FileNotFoundError):
        result = _walk_dirs('/path/to/source', trailing_slash_detector=is_remote_slash_significant)
