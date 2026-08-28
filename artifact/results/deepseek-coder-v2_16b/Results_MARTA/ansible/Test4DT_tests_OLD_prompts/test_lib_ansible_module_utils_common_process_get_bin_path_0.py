
import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.common.process import get_bin_path


def test_executable_not_found():
    with patch('os.environ', {'PATH': '/usr/local/bin:/usr/bin:/bin'}):
        with patch('os.path.exists', return_value=False):
            with pytest.raises(ValueError) as excinfo:
                get_bin_path('ls')
            assert 'Failed to find required executable "ls" in paths' in str(excinfo.value)
