
from pathlib import Path
import pytest
from isort.identify import Import

@pytest.fixture
def valid_import():
    return Import(line_number=1, indented=True, module="mymodule", cimport=False, attribute=None, alias=None)

def test_valid_case_2(valid_import):
    assert isinstance(valid_import, Import)
    assert valid_import.module == "mymodule"
    assert valid_import.cimport is False
    assert valid_import.attribute is None
    assert valid_import.alias is None
