
import pytest
from unittest.mock import patch
from flutils.packages import _build_version_bump_type, _BUMP_VERSION_MAJOR, _BUMP_VERSION_MINOR, _BUMP_VERSION_PATCH, _BUMP_VERSION_MINOR_ALPHA, _BUMP_VERSION_MINOR_BETA, _BUMP_VERSION_PATCH_ALPHA, _BUMP_VERSION_PATCH_BETA
from typing import Union

# Test valid major bump
def test_valid_major_bump():
    with patch('flutils.packages._build_version_bump_type', return_value=_BUMP_VERSION_MAJOR):
        assert _build_version_bump_type(0, None) == _BUMP_VERSION_MAJOR

# Test valid minor bump
def test_valid_minor_bump():
    with patch('flutils.packages._build_version_bump_type', return_value=_BUMP_VERSION_MINOR):
        assert _build_version_bump_type(1, None) == _BUMP_VERSION_MINOR

# Test valid patch bump
def test_valid_patch_bump():
    with patch('flutils.packages._build_version_bump_type', return_value=_BUMP_VERSION_PATCH):
        assert _build_version_bump_type(2, None) == _BUMP_VERSION_PATCH

# Test invalid prerelease raises ValueError
def test_invalid_prerelease():
    with pytest.raises(ValueError):
        _build_version_bump_type(1, 'gamma')

# Test major bump with prerelease raises ValueError
def test_major_with_prerelease():
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'beta')
