
from isort.identify import Import
import pytest

def test_edge_case_1():
    imp = Import(line_number=None, module=None, attribute=None, alias=None, indented=True)
    assert imp.indented == True
