# Module: pytutils.lazy.lazy_regex
import pytest
import re
from pytutils.lazy.lazy_regex import reset_compile

# Mocking the real_re_compile function for testing purposes
def mock_reset():
    pass

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Save the original re.compile before resetting
    global _real_re_compile
    _real_re_compile = re.compile
    
    # Replace re.compile with a mock function
    re.compile = mock_reset
    
    yield  # This is where the tests will run
    
    # Teardown: Restore re.compile to its original state
    re.compile = _real_re_compile

def test_reset_compile_first_call():
    """Test that reset_compile() restores re.compile to the initial state."""
    assert callable(re.compile)
    reset_compile()
    assert re.compile == _real_re_compile

def test_reset_compile_multiple_calls():
    """Test that multiple calls to reset_compile() do not affect its functionality."""
    reset_compile()
    for _ in range(5):  # Call reset_compile() multiple times
        reset_compile()
    assert re.compile == _real_re_compile
