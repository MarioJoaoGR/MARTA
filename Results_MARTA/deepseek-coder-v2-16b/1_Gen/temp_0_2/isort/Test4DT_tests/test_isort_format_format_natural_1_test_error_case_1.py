
# Import the format_natural function from the isort module
from isort.format import format_natural

def test_error_case_1():
    # Test case for a simple module name
    assert format_natural("numpy") == "import numpy"
    
    # Test case for an import statement with 'from' and 'import'
    assert format_natural("from math import sin") == "from math import sin"
    
    # Test case for a dotted notation
    assert format_natural("math.sin") == "from math import sin"
    
    # Test case for multiple imports separated by commas
    assert format_natural("from numpy import array, zeros") == "from numpy import array, zeros"
