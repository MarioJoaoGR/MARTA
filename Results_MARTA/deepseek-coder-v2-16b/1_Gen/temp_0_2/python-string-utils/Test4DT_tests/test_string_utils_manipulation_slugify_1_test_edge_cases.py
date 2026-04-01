
import re
from string_utils.manipulation import slugify

def test_edge_cases():
    # Test empty input string
    assert slugify('') == ''
    
    # Test input with only spaces
    assert slugify('   ') == ''
    
    # Test input with special characters and numbers
    assert slugify('Hello! This is a test.') == 'hello-this-is-a-test'
    
    # Test input with leading and trailing spaces
    assert slugify('  Hello World  ') == 'hello-world'
    
    # Test input with multiple separators
    assert slugify('Hello---World+++This--is---a---test') == 'hello-world-this-is-a-test'
    
    # Test input with uppercase letters
    assert slugify('HELLO WORLD') == 'hello-world'
    
    # Test input with unicode characters
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    
    # Test input with numbers only
    assert slugify('12345') == '12345'
    
    # Test input with special characters but no spaces or letters
    assert slugify('!@#$%^&*()') == ''
