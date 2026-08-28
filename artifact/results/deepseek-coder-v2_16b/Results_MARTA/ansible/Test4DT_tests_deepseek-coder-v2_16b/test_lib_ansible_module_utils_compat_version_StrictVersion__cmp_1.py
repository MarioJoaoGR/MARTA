
import pytest
from ansible.module_utils.compat.version import StrictVersion
import re

RE_FLAGS = re.IGNORECASE | re.ASCII

class TestStrictVersion:
    def setup(self):
        self.version = StrictVersion('1.0.4a3')
    
    def test_valid_input_happy_path(self):
        version = StrictVersion('1.0.4a3')
        assert str(version) == '1.0.4a3'
        assert version._cmp(StrictVersion('1.0.4')) > 0
        assert version._cmp(StrictVersion('1.0.4a3')) == 0
        assert version._cmp(StrictVersion('1.0.4b1')) < 0
    
    def test_edge_cases(self):
        with pytest.raises(ValueError) as e:
            StrictVersion(None)
        assert str(e.value) == "invalid version number 'None'"
        
        with pytest.raises(ValueError) as e:
            StrictVersion('')
        assert str(e.value) == "invalid version number ''"
    
    def test_invalid_input_error_handling(self):
        try:
            version = StrictVersion('invalid_version')
        except ValueError as e:
            print(e)
            assert str(e) == "invalid version number 'invalid_version'"
