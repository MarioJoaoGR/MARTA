
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.subversion import Subversion

def test_revert():
    with patch('ansible.modules.subversion.Subversion._exec', return_value=['Reverted somefile']):
        module = MagicMock()
        svn = Subversion(module, dest='path/to/destination', repo='http://example.com/repo', revision=None, username='user', password=None, svn_path='/usr/bin/svn', validate_certs=False)
        assert not svn.revert()

def test_revert_with_failure():
    with patch('ansible.modules.subversion.Subversion._exec', return_value=['Some other output']):
        module = MagicMock()
        svn = Subversion(module, dest='path/to/destination', repo='http://example.com/repo', revision=None, username='user', password=None, svn_path='/usr/bin/svn', validate_certs=False)
        assert svn.revert()
