
import pytest
import os
from ansible.module_utils.common.process import get_bin_path

# Test default behavior with no opt_dirs specified
def test_get_bin_path_default():
    bin_path = get_bin_path('ls')
    assert bin_path is not None