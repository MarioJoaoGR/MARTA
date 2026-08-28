
import pytest
from lib.ansible.module_utils.compat.version import StrictVersion, LooseVersion

# Test for valid case in StrictVersion
def test_valid_case_strict_version():
    from lib.ansible.module_utils.compat.version import StrictVersion
    v1 = StrictVersion('1.2.3')
    assert str(v1) == '1.2.3'

# Test for error case in StrictVersion
def test_error_case_strict_version():
    from lib.ansible.module_utils.compat.version import StrictVersion
    try:
        v_invalid = StrictVersion('1.2a3')
    except ValueError as e:
        assert str(e) == "invalid version number '1.2a3'"

# Test for error case in LooseVersion
def test_error_case_loose_version():
    from lib.ansible.module_utils.compat.version import LooseVersion
    try:
        v_invalid_loose = LooseVersion('1.2a3')
    except ValueError as e:
        assert str(e) == "invalid version number '1.2a3'"
