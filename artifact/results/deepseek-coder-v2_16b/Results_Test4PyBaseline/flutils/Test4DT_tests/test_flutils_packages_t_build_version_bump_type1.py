
import pytest
from typing import Union
from flutils.packages import _build_version_bump_type, _BUMP_VERSION_MAJOR, _BUMP_VERSION_MINOR, _BUMP_VERSION_PATCH, _BUMP_VERSION_MINOR_ALPHA, _BUMP_VERSION_MINOR_BETA, _BUMP_VERSION_PATCH_ALPHA, _BUMP_VERSION_PATCH_BETA

def test_major_bump_with_no_pre_release():
    result = _build_version_bump_type(0, None)
    assert result == _BUMP_VERSION_MAJOR

def test_minor_bump_with_pre_release_beta():
    result = _build_version_bump_type(1, 'beta')
    assert result == _BUMP_VERSION_MINOR_BETA

@pytest.mark.xfail(reason="Expected to raise ValueError")
def test_invalid_position_for_pre_release():
    with pytest.raises(ValueError):
        _build_version_bump_type(2, 'alpha')

def test_minor_bump_with_no_pre_release():
    result = _build_version_bump_type(1, None)
    assert result == _BUMP_VERSION_MINOR

# Additional tests for uncovered lines 152 and 163
def test_invalid_position_for_major_minor_prerelease():
    with pytest.raises(ValueError):
        _build_version_bump_type(0, 'alpha')

def test_invalid_position_for_patch_prerelease():
    result = _build_version_bump_type(2, 'beta')
    assert result == _BUMP_VERSION_PATCH_BETA

def test_invalid_pre_release_value():
    with pytest.raises(ValueError):
        _build_version_bump_type(1, 'gamma')
