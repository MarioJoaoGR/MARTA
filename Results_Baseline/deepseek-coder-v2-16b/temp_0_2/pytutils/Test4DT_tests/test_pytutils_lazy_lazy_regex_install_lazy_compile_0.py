
import pytest
from pytutils.lazy.lazy_regex import install_lazy_compile, reset_compile
import re

# Mocking the lazy_compile function for testing purposes
def mock_lazy_compile(*args, **kwargs):
    return "mocked_lazy_compile"

@pytest.fixture(autouse=True)
def setup():
    # Backup the original re.compile before setting it to mock_lazy_compile
    global original_compile
    original_compile = re.compile
    re.compile = mock_lazy_compile

@pytest.fixture(autouse=True)
def teardown():
    yield  # Ensure test runs are yielded so any cleanup can occur below this line
    # Reset re.compile to its original function after the test
    re.compile = original_compile

def test_install_lazy_compile():
    """Test that install_lazy_compile overrides re.compile with lazy_compile."""
    assert callable(original_compile), "Before installation, re.compile should be callable."
    install_lazy_compile()