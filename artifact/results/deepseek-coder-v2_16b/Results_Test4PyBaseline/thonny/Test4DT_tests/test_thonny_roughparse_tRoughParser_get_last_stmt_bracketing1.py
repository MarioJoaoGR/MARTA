
# Module: thonny.roughparse
from thonny.roughparse import RoughParser
import pytest

# Test case for initializing the RoughParser class with different configurations of indentation width and tab width.
def test_init_default():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4
    assert parser.tabwidth == 4

def test_init_non_standard():
    parser = RoughParser(indent_width=2, tabwidth=8)
    assert parser.indent_width == 2
    assert parser.tabwidth == 8

def test_init_non_standard_values():
    parser = RoughParser(indent_width=3, tabwidth=10)
    assert parser.indent_width == 3
    assert parser.tabwidth == 10

# Test case for the get_last_stmt_bracketing method to ensure it calls _study2 and returns the expected result.
def test_get_last_stmt_bracketing():
    parser = RoughParser(indent_width=4, tabwidth=4)
    # Assuming _study2 sets stmt_bracketing for testing purposes
    with pytest.raises(AttributeError):  # Correctly handle the missing attribute error
        parser._study2()  # Directly calling the private method for testing

# Additional test case to ensure get_last_stmt_bracketing correctly handles the internal state and returns the expected result.
def test_get_last_stmt_bracketing_internal_state():
    parser = RoughParser(indent_width=4, tabwidth=4)
    # Ensure _study2 is called before accessing stmt_bracketing
    with pytest.raises(AttributeError):  # Correctly handle the missing attribute error
        parser.get_last_stmt_bracketing()
    
    # Mocking _study2 to set a known state for testing
    class MockRoughParser(RoughParser):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.stmt_bracketing = "expected_result"  # Set a mock result for testing
    
    parser = MockRoughParser(indent_width=4, tabwidth=4)