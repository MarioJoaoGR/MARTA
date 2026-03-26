
import pytest

from isort.identify import Import


@pytest.fixture
def setup_valid_import():
    return Import(module="mymodule", attribute=None, alias=None, line_number=10, indented=True)

def test_valid_case_3(setup_valid_import):
    assert isinstance(setup_valid_import, Import)
    assert setup_valid_import.module == "mymodule"
    assert setup_valid_import.attribute is None
    assert setup_valid_import.alias is None
    assert setup_valid_import.line_number == 10
    assert setup_valid_import.indented is True
