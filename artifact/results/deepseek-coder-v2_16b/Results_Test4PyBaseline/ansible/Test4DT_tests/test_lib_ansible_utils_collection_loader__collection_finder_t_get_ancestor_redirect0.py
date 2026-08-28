
import pytest
from ansible.utils.collection_loader._collection_finder import _get_ancestor_redirect

# Test cases for _get_ancestor_redirect function

def test_basic_usage():
    redirected_package_map = {'pkg': 'new_pkg'}
    fullname = 'pkg.subpkg'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == 'new_pkg.subpkg', f"Expected 'new_pkg.subpkg', but got {result}"

def test_no_redirect_found():
    redirected_package_map = {'other_pkg': 'new_other_pkg'}
    fullname = 'another_pkg.subpkg'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None, f"Expected None, but got {result}"

def test_empty_redirect_map():
    redirected_package_map = {}
    fullname = 'pkg.subpkg'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result is None, f"Expected None, but got {result}"

def test_longer_full_name():
    redirected_package_map = {'pkg': 'new_pkg'}
    fullname = 'pkg.subpkg.another_subpkg'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == 'new_pkg.subpkg.another_subpkg', f"Expected 'new_pkg.subpkg.another_subpkg', but got {result}"

def test_single_level_package():
    redirected_package_map = {'pkg': 'new_pkg'}
    fullname = 'pkg'
    result = _get_ancestor_redirect(redirected_package_map, fullname)
    assert result == 'new_pkg', f"Expected 'new_pkg', but got {result}"
