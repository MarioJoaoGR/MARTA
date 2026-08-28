
import pytest
from ansible.module_utils.facts.packages import PkgMgr

# Test case for list_installed method in PkgMgr class
def test_list_installed():
    # Create a mock instance of PkgMgr (since it's abstract and cannot be instantiated directly)
    with pytest.raises(TypeError):
        pkg_mgr = PkgMgr()
