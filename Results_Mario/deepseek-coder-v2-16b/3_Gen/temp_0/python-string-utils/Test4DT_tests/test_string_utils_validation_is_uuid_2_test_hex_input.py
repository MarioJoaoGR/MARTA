
import pytest
from string_utils.validation import is_uuid
import re

# Assuming the module 'string_utils.validation' contains the UUID related functions
# If not, you need to adjust the import accordingly

@pytest.mark.parametrize("input_string, allow_hex, expected", [
    ('6f8aa2f9-686c-4ac3-8766-5712354a04cf', False, True),
    ('6f8aa2f9686c4ac387665712354a04cf', False, False),
    ('6f8aa2f9686c4ac387665712354a04cf', True, True),
])
def test_hex_input(input_string, allow_hex, expected):
    assert is_uuid(input_string, allow_hex) == expected
