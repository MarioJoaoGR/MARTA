
import pytest
from pathlib import Path
from isort.identify import Import

def test_import_statement():
    # Test case for default import statement without attribute or alias
    imp = Import(module="my_module", cimport=False, attribute=None, alias=None, line_number=10, indented=True)
    assert imp.line_number == 10
    assert imp.indented is True
    assert imp.module == "my_module"
    assert imp.attribute is None
    assert imp.alias is None
    assert imp.cimport is False
    
    # Check the statement method
    expected_statement = "import my_module"
    assert imp.statement() == expected_statement
