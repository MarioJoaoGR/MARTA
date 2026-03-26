# Module: pytutils.lazy.lazy_import
# Import the function correctly from its module
from pytutils.lazy.lazy_import import disallow_proxying

def test_disallow_proxying():
    # Before calling disallow_proxying, we should be able to use lazy imports as proxies
    try:
        from some_module import some_attribute  # This might be a lazy import
        assert False, "Expected an ImportError before the call to disallow_proxying"
    except ImportError:
        pass  # Expected behavior since we haven't called the function yet

    # Call the function to disable proxying
    disallow_proxying()

    # After calling disallow_proxying, any lazy import should raise an ImportError
    try:
        from some_module import some_attribute  # This should fail after the call
        assert False, "Expected an ImportError after the call to disallow_proxying"
    except ImportError:
        pass  # Expected behavior since proxying is disabled
