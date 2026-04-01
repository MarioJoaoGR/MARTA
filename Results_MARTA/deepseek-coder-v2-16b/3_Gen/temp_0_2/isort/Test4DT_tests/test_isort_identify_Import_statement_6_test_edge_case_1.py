
from isort.identify import Import
import pytest

def test_edge_case_1():
    with pytest.raises(TypeError):
        imp = Import(line_number=None, module=None, attribute=None, alias=None)
