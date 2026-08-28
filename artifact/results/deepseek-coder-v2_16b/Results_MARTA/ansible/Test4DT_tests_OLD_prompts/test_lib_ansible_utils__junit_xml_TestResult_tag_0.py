
import pytest
from ansible.utils._junit_xml import TestResult

def test_valid_inputs():
    with pytest.raises(TypeError):
        result = TestResult('PASS')
