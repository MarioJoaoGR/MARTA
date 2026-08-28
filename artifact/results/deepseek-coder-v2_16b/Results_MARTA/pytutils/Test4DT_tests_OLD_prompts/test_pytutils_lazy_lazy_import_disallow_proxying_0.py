
import pytest
from unittest.mock import patch
from pytutils.lazy.lazy_import import ScopeReplacer, disallow_proxying

def test_valid_input():
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        disallow_proxying()
        assert ScopeReplacer._should_proxy == False

def test_edge_case_none():
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        disallow_proxying()
        assert ScopeReplacer._should_proxy == False

def test_error_handling():
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        disallow_proxying()
        assert ScopeReplacer._should_proxy == False
