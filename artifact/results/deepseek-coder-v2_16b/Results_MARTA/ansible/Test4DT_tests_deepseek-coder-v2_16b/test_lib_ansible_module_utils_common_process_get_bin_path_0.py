
import os
import pytest
from ansible.module_utils.common.process import get_bin_path

@pytest.mark.skipif(os.name != 'posix', reason="This test is only applicable to POSIX systems")
def test_valid_case_find_ls():
    path = get_bin_path('ls')
    assert os.path.exists(path), f"Expected 'ls' executable not found at {path}"

@pytest.mark.skipif(os.name != 'posix', reason="This test is only applicable to POSIX systems")
def test_valid_case_find_curl_custom_dir():
    path = get_bin_path('curl', opt_dirs=['/usr/local/bin'])
    assert os.path.exists(path), f"Expected 'curl' executable not found at {path}"

@pytest.mark.skipif(os.name != 'posix', reason="This test is only applicable to POSIX systems")
def test_error_case_missing_executable():
    with pytest.raises(ValueError) as excinfo:
        get_bin_path('nonexistent')
    assert "Failed to find required executable" in str(excinfo.value), f"Expected ValueError not raised for missing executable"
