# Module: flutils.packages
import pytest
from flutils.packages import bump_version

# Test cases for bump_version function

def test_bump_patch_version():
    assert bump_version('1.2.3') == '1.2.4'
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.3.4', position=0) == '2.0'

def test_bump_patch_with_alpha():
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'
    assert bump_version('1.2.4a0', pre_release='a') == '1.2.4a1'
    assert bump_version('1.2.4a1', pre_release='b') == '1.2.4b0'

def test_no_change():
    assert bump_version('1.2.4a1') == '1.2.4'
    assert bump_version('1.2.4b0') == '1.2.4'

def test_bump_minor_with_alpha():
    assert bump_version('2.1.3', position=1, pre_release='a') == '2.2a0'

def test_bump_patch_from_beta():
    assert bump_version('1.2b0', position=2) == '1.2.1'

# Add more test cases to cover other scenarios and edge cases as needed
