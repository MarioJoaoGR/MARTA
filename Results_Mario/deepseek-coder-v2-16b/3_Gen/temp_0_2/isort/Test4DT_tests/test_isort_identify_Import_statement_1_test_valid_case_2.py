
from pathlib import Path
from isort.identify import Import

def test_valid_case_2():
    imp = Import(line_number=10, module='math', attribute='sin', alias=None, indented=True)
    assert imp.module == 'math'
    assert imp.attribute == 'sin'
    assert imp.alias is None
    assert imp.indented is True
