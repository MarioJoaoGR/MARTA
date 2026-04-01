
from isort.parse import import_type  # Importing the function from the module
import pytest

def test_empty_line():
    assert import_type("import os") == "straight"
    assert import_type("from math import sin") == "from"
    assert import_type("import sys # isort:skip") is None
    assert import_type("cimport some_module") == "straight"
    assert import_type("some other line") is None
