
import pytest
from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

# Test Scenario 1: Valid Case
def test_valid_case():
    redirected_package_map = {'pkg1': 'new_pkg1', 'pkg2': 'new_pkg2'}
    fullname = 'pkg1.subpkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == 'new_pkg1.subpkg.module'

# Test Scenario 2: Missing Case
def test_missing_case():
    redirected_package_map = {'pkgA': 'new_pkgA', 'pkgB': 'new_pkgB'}
    fullname = 'nonExistentPackage.subPkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None

# Test Scenario 3: Empty Case
def test_empty_case():
    redirected_package_map = {}
    fullname = 'pkgX.subPkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None
