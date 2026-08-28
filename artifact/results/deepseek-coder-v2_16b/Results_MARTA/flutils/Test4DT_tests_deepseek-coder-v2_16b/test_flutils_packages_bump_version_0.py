
import pytest
from flutils.packages import bump_version

def test_bump_major_version():
    assert bump_version('1.2.3', position=0) == '2.0'

def test_bump_minor_version():
    assert bump_version('1.2.3', position=1) == '1.3'

def test_bump_patch_version():
    assert bump_version('1.2.3') == '1.2.4'

def test_invalid_position():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=5)

def test_add_alpha_pre_release():
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'

def test_invalid_pre_release():
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')


def test_bump_minor_with_beta():
    assert bump_version('1.2.3', position=1, pre_release='b') == '1.3b0'