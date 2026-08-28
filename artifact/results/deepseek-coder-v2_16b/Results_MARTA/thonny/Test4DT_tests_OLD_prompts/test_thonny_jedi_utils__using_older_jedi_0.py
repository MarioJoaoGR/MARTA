
import pytest
from unittest.mock import patch
import jedi
from thonny.jedi_utils import _using_older_jedi

def test_valid_case_jedi_version_0_13():
    with patch('jedi.__version__', '0.13'):
        assert _using_older_jedi(jedi) is True

def test_valid_case_jedi_version_0_17():
    with patch('jedi.__version__', '0.17'):
        assert _using_older_jedi(jedi) is True

def test_invalid_case_newer_jedi_version():
    with patch('jedi.__version__', '0.18'):
        assert _using_older_jedi(jedi) is False
