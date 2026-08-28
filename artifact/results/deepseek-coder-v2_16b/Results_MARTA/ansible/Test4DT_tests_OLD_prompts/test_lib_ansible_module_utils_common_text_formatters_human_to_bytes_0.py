
import pytest
from ansible.module_utils.common.text.formatters import human_to_bytes



def test_invalid_input_raises_valueerror():
    with pytest.raises(ValueError):
        human_to_bytes('10Mb')
    with pytest.raises(ValueError):
        human_to_bytes('abc')