
import pytest
from string_utils.manipulation import slugify

def test_valid_input_standard():
    result = slugify('Top 10 Reasons To Love Dogs!!!')
    assert result == 'top-10-reasons-to-love-dogs'

def test_valid_input_custom_separator():
    result = slugify('Top 10 Reasons To Love Dogs!!!', separator='_')
    assert result == 'top_10_reasons_to_love_dogs'

def test_invalid_input_none():
    with pytest.raises(TypeError):
        slugify(None)
