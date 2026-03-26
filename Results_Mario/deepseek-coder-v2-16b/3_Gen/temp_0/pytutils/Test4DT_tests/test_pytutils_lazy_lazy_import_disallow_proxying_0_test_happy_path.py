
import pytest
from pytutils.lazy.lazy_import import ScopeReplacer

def disallow_proxying():
    """Disallow lazily imported modules to be used as proxies."""
    ScopeReplacer._should_proxy = False

@pytest.fixture(autouse=True)
def setup_disallow_proxying():
    disallow_proxying()

def test_happy_path():
    # Your test code here
    pass  # Replace this with your actual test logic
