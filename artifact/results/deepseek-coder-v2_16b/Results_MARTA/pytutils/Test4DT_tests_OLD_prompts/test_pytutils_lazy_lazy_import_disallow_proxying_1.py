
import pytest
from unittest.mock import patch
from pytutils.lazy.lazy_import import ScopeReplacer, disallow_proxying

def test_valid_input():
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        assert ScopeReplacer._should_proxy is True
        disallow_proxying()
        assert ScopeReplacer._should_proxy is False

def test_none_input():
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        assert ScopeReplacer._should_proxy is True
        disallow_proxying()
        assert ScopeReplacer._should_proxy is False
