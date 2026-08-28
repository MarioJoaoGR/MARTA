
import pytest
from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

# Test for valid case where a redirect exists in redirected_package_map
def test_valid_case():
    redirected_package_map = {'pkg1': 'new_pkg1', 'pkg2': 'new_pkg2'}
    fullname = 'pkg1.subpkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == 'new_pkg1.subpkg.module'

# Test for case where no redirect is found in redirected_package_map
def test_missing_case():
    redirected_package_map = {}
    fullname = 'nonExistentPackage.subPkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None

# Test for case where redirected_package_map is empty
def test_empty_map_case():
    redirected_package_map = {}
    fullname = 'pkgX.subPkg.module'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None
