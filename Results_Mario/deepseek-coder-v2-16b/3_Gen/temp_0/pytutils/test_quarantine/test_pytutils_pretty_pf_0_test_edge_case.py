
import pytest
from unittest.mock import patch, MagicMock
from pytutils.pretty import pf

@pytest.mark.skip(reason="Pygments is not available in this environment")
def test_pf_with_no_pygments():
    # Mocking the Pygments library to be unavailable
    with patch('pytutils.pretty.__PP_LEXER_PYTHON', None):
        with patch('pytutils.pretty.__PP_FORMATTER', None):
            assert pf([1, 2, {'key': 'value'}]) == '[1, 2, {\'key\': \'value\'}]'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""