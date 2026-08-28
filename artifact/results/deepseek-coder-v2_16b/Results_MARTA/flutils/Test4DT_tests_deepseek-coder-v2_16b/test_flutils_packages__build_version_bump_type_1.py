
import pytest
from flutils.packages import _build_version_bump_type, _BUMP_VERSION_MAJOR, _BUMP_VERSION_MINOR, _BUMP_VERSION_PATCH, _BUMP_VERSION_MINOR_ALPHA, _BUMP_VERSION_MINOR_BETA, _BUMP_VERSION_PATCH_ALPHA, _BUMP_VERSION_PATCH_BETA
from typing import Union


def test_major_bump_with_no_prerelease():
    result = _build_version_bump_type(0, None)
    assert result == _BUMP_VERSION_MAJOR

def test_minor_bump_with_alpha_prerelease():
    result = _build_version_bump_type(1, 'alpha')
    assert result == _BUMP_VERSION_MINOR_ALPHA

def test_patch_bump_with_beta_prerelease():
    result = _build_version_bump_type(2, 'beta')
    assert result == _BUMP_VERSION_PATCH_BETA

def test_minor_bump_with_no_prerelease():
    result = _build_version_bump_type(1, None)
    assert result == _BUMP_VERSION_MINOR

def test_patch_bump_with_no_prerelease():
    result = _build_version_bump_type(2, None)
    assert result == _BUMP_VERSION_PATCH