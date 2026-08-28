
import pytest
from ansible.utils._junit_xml import TestResult



def test_invalid_input():
    with pytest.raises(TypeError):
        TestResult('INVALID', 'Invalid output')