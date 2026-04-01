
import pytest
from unittest.mock import patch
from string_utils.manipulation import slugify

@pytest.mark.parametrize("input_string, expected", [
    ('Top 10 Reasons To Love Dogs!!!', 'top-10-reasons-to-love-dogs'),
    ('Mönstér Mägnët', 'monster-magnet'),
])
def test_valid_slugify(input_string, expected):
    with patch('string_utils.manipulation.asciify', return_value=expected):
        result = slugify(input_string)
        assert result == expected
