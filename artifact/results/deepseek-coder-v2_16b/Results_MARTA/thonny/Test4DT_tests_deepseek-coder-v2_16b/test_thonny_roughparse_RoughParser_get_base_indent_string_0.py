
import pytest
from thonny.roughparse import RoughParser



def test_no_newline_at_end():
    parser = RoughParser(indent_width=4, tabwidth=4)
    with pytest.raises(AssertionError):
        parser.set_str('def example():')