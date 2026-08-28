
import pytest
from lib.ansible.module_utils.compat.version import StrictVersion, LooseVersion

# Test for valid case using StrictVersion
def test_valid_case_strict_version():
    from lib.ansible.module_utils.compat.version import StrictVersion
    v1 = StrictVersion('1.0.4a3')
    assert str(v1) == '1.0.4a3'

# Test for error case with invalid input to StrictVersion
def test_error_case_strict_version():
    from lib.ansible.module_utils.compat.version import StrictVersion
    try:
        v = StrictVersion('invalid_version')
        assert False, 'Expected ValueError not raised'
    except ValueError as e:
        print(e)  # Expected output will be "invalid version number 'invalid_version'"

# Test for error case with invalid input to LooseVersion
def test_error_case_loose_version():
    from lib.ansible.module_utils.compat.version import LooseVersion
    try:
        v = LooseVersion('invalid_version')
        assert False, 'Expected ValueError not raised'
    except ValueError as e:
        print(e)  # Expected output will be "invalid version number 'invalid_version'"
