
import pytest
from pytutils.env import expand
import os

def test_expand():
    # Test expanding a user home directory placeholder
    assert expand("~/Documents") == os.path.expanduser("~/Documents")
    
    # Mock environment variables for testing
    os.environ['USER'] = 'admin'
    os.environ['HOME'] = '/root'
    
    # Test expanding a shell-style variable
    assert expand("$USER/Desktop") == "admin/Desktop"
    
    # Test expanding the tilde character to user home directory
    assert expand("~") == os.path.expanduser("~")
