
from unittest.mock import patch
from pytutils.lazy.lazy_import import ScopeReplacer

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies.

    Calling this function might cause problems with concurrent imports
    in multithreaded environments, but will help detecting wasteful
    indirection, so it should be called when executing unit tests.

    Only lazy imports that happen after this call are affected.
    """
    ScopeReplacer._should_proxy = False

def test_happy_path():
    with patch('pytutils.lazy.lazy_import.ScopeReplacer._should_proxy', new=True):
        disallow_proxying()
        assert not ScopeReplacer._should_proxy, "The _should_proxy attribute should be set to False after calling disallow_proxying."
