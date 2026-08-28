
import pytest
from ansible.modules.subversion import Subversion
from unittest.mock import patch
import subprocess

@pytest.fixture(scope="module")
def svn_instance():
    module = type('AnsibleModule', (object,), {})()
    return Subversion(module, dest='path/to/destination', repo='http://example.com/repo', revision='HEAD', username='user', password=None, svn_path='/usr/bin/svn', validate_certs=False)

def test_valid_export(svn_instance):
    with patch('subprocess.run') as mock_run:
        # Mock the subprocess call to return a successful result
        mock_run.return_value = subprocess.CompletedProcess(['/usr/bin/svn', 'export', '-r', 'HEAD', 'http://example.com/repo', 'path/to/destination'], returncode=0)
        
        svn_instance.export()
        
        # Assert that the command was called with the expected arguments
        mock_run.assert_called_with(['/usr/bin/svn', 'export', '-r', 'HEAD', 'http://example.com/repo', 'path/to/destination'], check=True)

def test_force_export(svn_instance):
    with patch('subprocess.run') as mock_run:
        # Mock the subprocess call to return a successful result
        mock_run.return_value = subprocess.CompletedProcess(['/usr/bin/svn', 'export', '--force', '-r', 'HEAD', 'http://example.com/repo', 'path/to/destination'], returncode=0)
        
        svn_instance.export(force=True)
        
        # Assert that the command was called with the expected arguments
        mock_run.assert_called_with(['/usr/bin/svn', 'export', '--force', '-r', 'HEAD', 'http://example.com/repo', 'path/to/destination'], check=True)

def test_invalid_export(svn_instance):
    with patch('subprocess.run') as mock_run:
        # Mock the subprocess call to return a failure result
        mock_run.return_value = subprocess.CompletedProcess(['/usr/bin/svn', 'export', '-r', 'HEAD', 'invalid-url', 'path/to/destination'], returncode=1)
        
        with pytest.raises(subprocess.CalledProcessError):
            svn_instance.export()
