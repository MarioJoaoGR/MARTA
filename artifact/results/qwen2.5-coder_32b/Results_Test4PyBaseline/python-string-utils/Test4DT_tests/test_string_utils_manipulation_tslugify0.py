# Module: string_utils.manipulation
import pytest
from string_utils.manipulation import slugify, InvalidInputError

def test_slugify_basic():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'

def test_slugify_custom_separator():
    assert slugify('Mönstér Mägnët', '_') == 'monster_magnet'

def test_slugify_numbers_and_special_chars():
    assert slugify('2023 @ New Year Celebration!') == '2023-new-year-celebration'

def test_slugify_mixed_case_and_punctuation():
    assert slugify('HELLO, WORLD!!!') == 'hello-world'

def test_slugify_multiple_spaces():
    assert slugify('Multiple   spaces   here') == 'multiple-spaces-here'

def test_slugify_no_alphanumeric_chars():
    assert slugify('!!!###$$$') == ''

def test_slugify_empty_string():
    assert slugify('') == ''

def test_slugify_invalid_input_type():
    with pytest.raises(InvalidInputError):
        slugify(12345)

def test_slugify_none_input():
    with pytest.raises(InvalidInputError):
        slugify(None)

def test_slugify_only_special_chars_with_separator():
    assert slugify('!!!###$$$', '_') == ''
