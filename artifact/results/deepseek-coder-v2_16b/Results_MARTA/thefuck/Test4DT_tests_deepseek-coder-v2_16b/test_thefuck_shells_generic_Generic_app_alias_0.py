
import pytest
from thefuck.shells.generic import Generic


def test_edge_case_none():
    generic_shell = Generic()
    with pytest.raises(TypeError):
        generic_shell.app_alias()
