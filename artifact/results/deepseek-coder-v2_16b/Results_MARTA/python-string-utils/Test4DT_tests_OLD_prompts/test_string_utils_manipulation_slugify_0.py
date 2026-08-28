
import pytest
from unittest.mock import patch
from string_utils.manipulation import slugify, InvalidInputError

# Test scenarios
def test_valid_slugify_basic():
    result = slugify('Top 10 Reasons To Love Dogs!!!')
    assert result == 'top-10-reasons-to-love-dogs'

def test_valid_slugify_custom_separator():
    result = slugify('Top 10 Reasons To Love Dogs!!!', separator='_')
    assert result == 'top_10_reasons_to_love_dogs'

def test_invalid_slugify_input():
    with pytest.raises(InvalidInputError):
        slugify(42)
