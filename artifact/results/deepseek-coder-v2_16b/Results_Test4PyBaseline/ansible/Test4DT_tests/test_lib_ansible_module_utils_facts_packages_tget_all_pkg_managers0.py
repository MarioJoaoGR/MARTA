
import pytest
from ansible.module_utils.facts.packages import get_all_pkg_managers
from unittest.mock import patch

# Mocking the necessary classes and functions for testing
class PkgMgr: pass
class CLIMgr(PkgMgr): pass
class LibMgr(PkgMgr): pass

def get_all_subclasses(cls):
    return [subcls for subcls in cls.__subclasses__() if subcls not in (CLIMgr, LibMgr)]

@patch('ansible.module_utils.facts.packages.get_all_subclasses', side_effect=lambda cls: [PkgMgr, CLIMgr, LibMgr])
def test_get_all_pkg_managers(mock_get_all_subclasses):
    # Test when no subclasses are filtered out
    mock_get_all_subclasses.return_value = [PkgMgr(), CLIMgr(), LibMgr()]
    
    pkg_managers = get_all_pkg_managers()
    assert isinstance(pkg_managers, dict)
    assert len(pkg_managers) == 3  # PkgMgr, CLIMgr, and LibMgr should be in the dictionary since none are filtered out
    assert set(pkg_managers.keys()) == {'pkgmgr', 'climgr', 'libmgr'}  # All package managers should be included

    # Test when subclasses are filtered out
    mock_get_all_subclasses.return_value = [CLIMgr(), LibMgr()]
    
    pkg_managers = get_all_pkg_managers()
    assert isinstance(pkg_managers, dict)