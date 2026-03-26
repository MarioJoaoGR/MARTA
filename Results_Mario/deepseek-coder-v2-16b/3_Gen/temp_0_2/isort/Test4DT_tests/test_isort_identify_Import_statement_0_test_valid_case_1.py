
from pathlib import Path
from isort.identify import Import

def test_valid_case_1():
    imp = Import(line_number=10, module='math', attribute=None, alias=None, indented=True)
    assert imp.statement() == "import math"
