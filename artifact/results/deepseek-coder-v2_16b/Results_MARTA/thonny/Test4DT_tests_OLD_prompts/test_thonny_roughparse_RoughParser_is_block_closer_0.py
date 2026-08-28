
import pytest
from unittest.mock import patch, MagicMock
from thonny.roughparse import RoughParser


def test_error_case():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the constructor expects two arguments (indent_width and tabwidth), but no arguments are provided.
        RoughParser()