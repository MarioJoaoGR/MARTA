
import pytest
from flutils.packages import bump_version

def test_valid_case_1():
    assert bump_version('1.2.3') == '1.2.4'

def test_valid_case_2():
    assert bump_version('1.2.3', position=1) == '1.3'

def test_valid_case_3():
    assert bump_version('1.3.4', position=0) == '2.0'



def test_error_case_out_of_range_position():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=5)

def test_error_case_invalid_prerelease():
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')