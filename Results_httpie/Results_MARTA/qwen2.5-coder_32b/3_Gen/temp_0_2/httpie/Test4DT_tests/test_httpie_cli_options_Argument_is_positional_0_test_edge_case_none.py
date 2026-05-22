
import pytest
from unittest.mock import patch
from httpie.cli.options import Argument

def test_edge_case_none():
    with pytest.raises(TypeError):
        arg = Argument()
        arg.is_positional()
