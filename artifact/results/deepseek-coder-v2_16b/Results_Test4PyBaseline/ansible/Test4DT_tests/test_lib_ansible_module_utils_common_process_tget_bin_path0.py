
import pytest
import os
from ansible.module_utils.common.process import get_bin_path

# Test finding a system executable in standard directories
def test_get_bin_path_found():
    assert get_bin_path('ls') is not None

# Test finding a specific executable in custom directories
def test_get_bin_path_custom_dirs():
    with pytest.raises(ValueError) as exc_info:
        get_bin_path('ls', opt_dirs=['/nonexistent/dir1', '/nonexistent/dir2'])
    assert str(exc_info.value) == 'Failed to find required executable "ls" in paths: /nonexistent/dir1:/nonexistent/dir2'

# Test handling the absence of an executable (raises ValueError)
def test_get_bin_path_not_found():
    with pytest.raises(ValueError) as exc_info:
        get_bin_path('nonexistent_executable')
    assert str(exc_info.value) == 'Failed to find required executable "nonexistent_executable" in paths: /usr/local/sbin:/usr/sbin:/sbin:/usr/bin:/bin'

# Test deprecated required parameter raises TypeError
def test_get_bin_path_required_deprecated():
    with pytest.raises(TypeError):
        get_bin_path('ls', opt_dirs=[], required=True)
