
from isort.parse import import_type  # Importing from the correct module

def test_skipped_by_noqa():
    assert import_type("import os") == 'straight'
    assert import_type("from math import sin") == 'from'
    assert import_type("import sys # isort:skip") is None
    assert import_type("cimport some_module") == 'straight'
