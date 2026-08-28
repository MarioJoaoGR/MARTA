
import pytest
from ansible.module_utils.common.text.formatters import bytes_to_human

# Scenario 1: Test standard input with default isbits=False (setup: size = 1024)
def test_valid_input_default_isbits():
    assert bytes_to_human(1024) == '1.00 KB'

# Scenario 2: Test standard input with specified unit (setup: size = 1500, unit='B')
def test_valid_input_specified_unit():
    assert bytes_to_human(1500, unit='B') == '1.46 KB'

# Scenario 3: Test handling of None input (setup: size = None)
def test_invalid_input_none():
    with pytest.raises(TypeError):
        bytes_to_human(None)
