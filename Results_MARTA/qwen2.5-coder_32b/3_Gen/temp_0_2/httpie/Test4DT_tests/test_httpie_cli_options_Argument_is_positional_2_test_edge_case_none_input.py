
import pytest
from unittest.mock import patch
from httpie.cli.options import Argument

def test_edge_case_none_input():
    with pytest.raises(TypeError):
        arg = None
        argument = Argument()
        argument.is_positional()
