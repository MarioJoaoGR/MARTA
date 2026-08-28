
import re
from string_utils.manipulation import slugify

def test_slugify_with_spaces_and_punctuation():
    # Test with a string containing spaces and punctuation
    result = slugify('Top 10 Reasons To Love Dogs!!!')
    assert result == 'top-10-reasons-to-love-dogs'

def test_slugify_with_custom_separator():
    # Test with a custom separator
    result = slugify('Mönstér Mägnët', '_')
    assert result == 'monster_magnet'

def test_slugify_with_special_characters():
    # Test with special characters
    result = slugify('Hello, World! This is a test.')
    assert result == 'hello-world-this-is-a-test'

def test_slugify_with_numbers_and_mixed_case():
    # Test with numbers and mixed case
    result = slugify('Python3.8 is Awesome!!')
    assert result == 'python3-8-is-awesome'

def test_slugify_with_no_letters_or_numbers():
    # Test with no letters or numbers
    result = slugify('!!!###$$$%%%^^^&&&***((()))___+++===---~~~')
    assert result == ''

def test_slugify_with_only_spaces():
    # Test with only spaces
    result = slugify('     ')
    assert result == ''

def test_slugify_with_multiple_separators():
    # Test with multiple separators
    result = slugify('This--is__a___test---string')
    assert result == 'this-is-a-test-string'

def test_slugify_with_leading_and_trailing_punctuation():
    # Test with leading and trailing punctuation
    result = slugify('!!!Hello World!!!')
    assert result == 'hello-world'

def test_slugify_with_unicode_characters():
    # Test with unicode characters
    result = slugify('Café Münster')
    assert result == 'cafe-munster'
