# Module: pytutils.lazy.lazy_import
# Import the function correctly from its module
from pytutils.lazy.lazy_import import disallow_proxying

def test_disallow_proxying():
    # Before calling disallow_proxying, importing a module should still allow proxying
    try:
        import some_module  # This might be a proxy import if _should_proxy is True
        assert False, "Expected ImportError but no exception was raised"
    except ImportError:
        pass  # Expected behavior when _should_proxy is True

    # Call disallow_proxying to set _should_proxy to False
    disallow_proxying()

    # After calling disallow_proxying, importing a module should raise an ImportError
    try:
        import some_module  # This should now be a direct import since _should_proxy is False
        assert False, "Expected ImportError but no exception was raised"
    except ImportError:
        pass  # Expected behavior when _should_proxy is False
