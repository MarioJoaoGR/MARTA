
import pytest
from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

# Test scenario 1: valid case
def test_valid_case():
    redirected_package_map = {'pkg1': 'new_pkg1', 'pkg2': 'new_pkg2'}
    fullname = 'pkg1.subpkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == 'new_pkg1.subpkg.module'

# Test scenario 2: no redirect found
def test_no_redirect():
    redirected_package_map = {}
    fullname = 'nonExistentPackage.subPkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None

# Test scenario 3: empty redirect map
def test_empty_map():
    redirected_package_map = {}
    fullname = 'pkgX.subPkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None
