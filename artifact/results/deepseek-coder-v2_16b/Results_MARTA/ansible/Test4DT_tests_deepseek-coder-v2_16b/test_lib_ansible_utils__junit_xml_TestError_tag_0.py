
import pytest
from ansible.utils._junit_xml import TestError



def test_invalid_input():
    with pytest.raises(TypeError):
        test_instance = TestError()
        test_instance.tag()