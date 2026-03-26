
import pytest
from isort.format import format_natural

def test_valid_case_2():
    assert format_natural("numpy") == "import numpy"
    assert format_natural("math.sin") == "from math import sin"
    assert format_natural("from numpy import array, zeros") == "from numpy import array, zeros"
    assert format_natural("from math import cos, tan") == "from math import cos, tan"
    assert format_natural("numpy.array") == "from numpy import array"
    assert format_natural("numpy.random.rand") == "from numpy.random import rand"
    with pytest.raises(AssertionError):
        assert format_natural("math.sqrt(3)") == "from math import sqrt"
