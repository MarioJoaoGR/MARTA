
import pytest
from ansible.module_utils.facts.packages import PkgMgr

# Test case for checking if list_installed method is abstract and cannot be instantiated directly
def test_abstract_pkg_mgr():
    with pytest.raises(TypeError):
        pkg_mgr = PkgMgr()
