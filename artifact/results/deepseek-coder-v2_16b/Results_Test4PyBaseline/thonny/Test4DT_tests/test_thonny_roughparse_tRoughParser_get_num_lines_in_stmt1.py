
import pytest
from thonny.roughparse import RoughParser

# Test initialization of RoughParser with specific indentation and tab widths
def test_roughparser_initialization():
    parser = RoughParser(indent_width=4, tabwidth=4)
    assert parser.indent_width == 4

# Test get_num_lines_in_stmt method when goodlines is not yet populated
def test_get_num_lines_in_stmt_empty():
    parser = RoughParser(indent_width=4, tabwidth=4)
    with pytest.raises(AttributeError):
        assert parser.get_num_lines_in_stmt()

# Test get_num_lines_in_stmt method when goodlines has at least two elements
def test_get_num_lines_in_stmt_populated():
    parser = RoughParser(indent_width=4, tabwidth=4)
    # Assuming there are other methods to populate goodlines for testing
    parser.goodlines = [0, 10]  # Example values, adjust as necessary