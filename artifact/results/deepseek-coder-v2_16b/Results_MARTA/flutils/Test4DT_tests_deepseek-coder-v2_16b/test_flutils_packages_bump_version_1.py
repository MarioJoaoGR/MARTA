
import pytest
from flutils.packages import bump_version

# Test basic version bump with default position and no pre-release
def test_valid_input_basic():
    assert bump_version('1.2.3') == '1.2.4'

# Test version bump to a specific position, including minor and major
def test_valid_input_specific_position():
    assert bump_version('1.2.3', position=1) == '1.3'
    assert bump_version('1.2.3', position=0) == '2.0'

# Test raising ValueError for invalid version string
def test_invalid_version_string():
    with pytest.raises(ValueError):
        bump_version('invalid-version')

# Test raising ValueError for invalid position
def test_invalid_position():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=5)

# Test raising ValueError for invalid pre-release identifier
def test_invalid_pre_release():
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')
