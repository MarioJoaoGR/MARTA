
import pytest
import re
from pytutils.lazy.lazy_regex import _real_re_compile

@pytest.fixture(autouse=True)
def reset_re_compile():
    """Fixture to reset re.compile to its original implementation before each test."""
    original_compile = re.compile
    yield  # Run the tests
    re.compile = original_compile  # Reset re.compile after the test

def test_valid_input():
    from pytutils.lazy.lazy_regex import reset_compile
    reset_compile()
    assert re.compile == _real_re_compile
