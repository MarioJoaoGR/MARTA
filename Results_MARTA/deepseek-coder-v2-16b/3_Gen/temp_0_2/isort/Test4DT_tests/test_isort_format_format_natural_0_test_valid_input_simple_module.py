
import pytest
from isort.format import format_natural

def test_valid_input_simple_module():
    # Test when input is a simple module name
    assert format_natural("math") == "import math"
    
    # Test when input contains dots and should be formatted to 'from ... import ...'
    assert format_natural("math.sin") == "from math import sin"
    
    # Test when input is already in the correct format (should return as is)
    assert format_natural("from math import sin") == "from math import sin"
    assert format_natural("import math") == "import math"
