
import pytest
from thonny.roughparse import RoughParser

def test_error_case():
    with pytest.raises(TypeError):
        parser = RoughParser()  # This should raise a TypeError because the constructor expects two arguments (indent_width and tabwidth)
