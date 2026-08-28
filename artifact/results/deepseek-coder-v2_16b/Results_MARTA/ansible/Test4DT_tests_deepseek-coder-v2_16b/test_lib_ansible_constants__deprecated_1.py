
import pytest
from unittest.mock import patch
import sys

def _deprecated(msg, version):
    ''' display is not guaranteed here, nor it being the full class, but try anyways, fallback to sys.stderr.write '''
    try:
        from ansible.utils.display import Display
        Display().deprecated(msg, version=version)
    except Exception:
        sys.stderr.write(' [DEPRECATED] %s, to be removed in %s\n' % (msg, version))

# Test for valid inputs

# Test for edge cases

# Test for invalid inputs
def test_invalid_inputs():
    with pytest.raises(TypeError):
        _deprecated("This function is deprecated.", "2.0", "extra_arg")