
import pytest
from unittest.mock import patch
from flutils.packages import _build_version_bump_type, _BUMP_VERSION_MAJOR, _BUMP_VERSION_MINOR, _BUMP_VERSION_PATCH, _BUMP_VERSION_MINOR_ALPHA, _BUMP_VERSION_MINOR_BETA, _BUMP_VERSION_PATCH_ALPHA, _BUMP_VERSION_PATCH_BETA
from typing import Union

# Test valid major bump with no pre-release
def test_valid_major_bump():
    assert _build_version_bump_type(0, None) == _BUMP_VERSION_MAJOR

# Test valid minor bump with a pre-release (alpha)
def test_valid_minor_bump_with_prerelease():
    assert _build_version_bump_type(1, 'alpha') == _BUMP_VERSION_MINOR_ALPHA

# Test valid patch bump with a pre-release (beta)
def test_valid_patch_bump_with_prerelease():
    assert _build_version_bump_type(2, 'beta') == _BUMP_VERSION_PATCH_BETA

# Test invalid pre-release value that raises ValueError
def test_invalid_prerelease_value():
    with pytest.raises(ValueError):
        _build_version_bump_type(1, 'gamma')

# Test major bump with a pre-release which should raise ValueError
def test_major_bump_with_prerelease():
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'beta')

# Test valid minor bump without a pre-release
def test_valid_minor_bump_without_prerelease():
    assert _build_version_bump_type(1, None) == _BUMP_VERSION_MINOR

# Test valid patch bump without a pre-release
def test_valid_patch_bump_without_prerelease():
    assert _build_version_bump_type(2, None) == _BUMP_VERSION_PATCH
