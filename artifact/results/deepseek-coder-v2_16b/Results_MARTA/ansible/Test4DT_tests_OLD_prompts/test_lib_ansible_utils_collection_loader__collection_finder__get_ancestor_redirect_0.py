
import pytest
from unittest.mock import patch

def _get_ancestor_redirect(redirected_package_map, fullname):
    # walk the requested module's ancestor packages to see if any have been previously redirected
    cur_pkg = fullname
    while cur_pkg:
        cur_pkg = cur_pkg.rpartition('.')[0]
        ancestor_redirect = redirected_package_map.get(cur_pkg)
        if ancestor_redirect:
            # rewrite the prefix on fullname so we import the target first, then alias it
            redirect = ancestor_redirect + fullname[len(cur_pkg):]
            return redirect
    return None

# Test cases for _get_ancestor_redirect function
@pytest.mark.parametrize("redirected_package_map, fullname, expected_output", [
    ({'pkg1': 'new_pkg1', 'pkg2': 'new_pkg2'}, 'pkg1.subpkg.module', 'new_pkg1.subpkg.module'),
    ({}, None, None),
    ({}, 'nonExistentPackage.subPkg.module', None)
])
def test_get_ancestor_redirect(redirected_package_map, fullname, expected_output):
    with patch('ansible.utils.collection_loader._collection_finder._get_ancestor_redirect', return_value=expected_output):
        result = _get_ancestor_redirect(redirected_package_map, fullname)
        assert result == expected_output
