
import pytest
from pkg_resources import Requirement
from ansible.modules.pip import _is_present, Package




def test_edge_case_none():
    installed_pkgs = None
    req = None
    with pytest.raises(TypeError):
        assert _is_present(None, req, installed_pkgs, None) == False

