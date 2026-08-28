
import os
import pytest
from ansible.plugins.action import copy as action_copy

@pytest.fixture
def setup_walk_dirs():
    def _setup_walk_dirs(topdir, base_path=None, local_follow=False, trailing_slash_detector=None):
        return action_copy._walk_dirs(topdir, base_path, local_follow, trailing_slash_detector)
    return _setup_walk_dirs

def test_basic_usage(tmp_path, setup_walk_dirs):
    # Create a temporary directory structure for testing
    src = tmp_path / 'src'
    dst = tmp_path / 'dst'
    src.mkdir()
    (src / 'file1').touch()
    (src / 'dir1').mkdir()
    (src / 'dir1' / 'file2').touch()
    
    result = setup_walk_dirs(str(src))
    
    assert isinstance(result, dict)
    assert 'files' in result
    assert 'directories' in result
    assert 'symlinks' in result
    assert len(result['files']) == 2  # Corrected to match the actual number of files
    assert len(result['directories']) == 1
    assert len(result['symlinks']) == 0
    
    # Check if the paths are correct