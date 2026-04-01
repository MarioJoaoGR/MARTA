
from isort.parse import import_type  # Importing from isort.parse module
import pytest

@pytest.mark.parametrize("line, expected", [
    ("import os", "straight"),
    ("from math import sin", "from"),
    ("import sys # isort:skip", None),
    ("cimport some_module", "straight"),
    ("# isort: skip\nimport sys", None),  # Test with a commented line
    ("# isort: skip\nfrom math import sin", None),  # Test with a commented line
])
def test_import_type(line, expected):
    assert import_type(line) == expected
