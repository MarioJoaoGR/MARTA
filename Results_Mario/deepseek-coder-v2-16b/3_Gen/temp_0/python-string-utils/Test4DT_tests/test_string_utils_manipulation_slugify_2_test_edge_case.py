
import pytest
from string_utils.manipulation import slugify

def test_edge_case():
    # Test case for edge cases such as empty strings or very short strings
    assert slugify('') == ''
    assert slugify(' ') == ''
    assert slugify('   ') == ''
    assert slugify('a') == 'a'
    assert slugify('A') == 'a'
    assert slugify('Hello World!') == 'hello-world'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
