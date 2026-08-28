
import pytest
from isort.format import format_natural

def test_format_natural_basic():
    assert format_natural("math") == "import math"
    assert format_natural("from math import sin") == "from math import sin"
    assert format_natural("numpy as np") == "import numpy as np"
    assert format_natural("os.path.join") == "from os.path import join"
