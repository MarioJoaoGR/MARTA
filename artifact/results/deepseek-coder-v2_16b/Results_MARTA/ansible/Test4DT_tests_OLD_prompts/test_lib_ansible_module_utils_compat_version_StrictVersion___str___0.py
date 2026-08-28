
import pytest
from ansible.module_utils.compat.version import StrictVersion

class TestStrictVersion:
    def test_valid_version(self):
        v = StrictVersion('0.5a1')
        assert str(v) == '0.5a1'

    def test_valid_version_without_prerelease(self):
        v = StrictVersion('0.9.6')
        assert str(v) == '0.9.6'

    def test_invalid_version(self):
        with pytest.raises(ValueError):
            v = StrictVersion('1')

    def test_valid_version_with_prerelease(self):
        v = StrictVersion('1.0.4b1')
        assert str(v) == '1.0.4b1'

    def test_equal_versions(self):
        v1 = StrictVersion('0.5a1')
        v2 = StrictVersion('0.5a1')
        assert v1 == v2

    def test_greater_version(self):
        v1 = StrictVersion('0.9.6')
        v2 = StrictVersion('0.5a1')
        assert v1 > v2

    def test_lesser_version(self):
        v1 = StrictVersion('0.4.0')
        v2 = StrictVersion('0.9.6')
        assert v1 < v2
