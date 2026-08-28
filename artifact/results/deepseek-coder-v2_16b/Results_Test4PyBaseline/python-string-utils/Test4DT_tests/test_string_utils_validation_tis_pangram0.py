
# Module: string_utils.validation
import pytest
from string_utils.validation import is_pangram
import re
import string

# Assuming SPACES_RE and is_full_string are defined elsewhere in the module or imported from a standard library
SPACES_RE = re.compile(r'\s+')

def test_is_pangram():
    # Test case: Basic pangram check
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    
    # Test case: Non-pangram check
    assert is_pangram('hello world') == False
    
    # Test case: Edge Case - Empty String (assuming `is_full_string` rejects empty strings)
    assert is_pangram('') == False
    
    # Test case: Edge Case - Whitespace Only (assuming `is_full_string` rejects whitespace-only strings)
    assert is_pangram('     ') == False
    
    # Test case: Case Insensitivity
    assert is_pangram('A quick brown fox jumps over the lazy dog') == True
    
    # Test case: Including Numbers and Special Characters
    assert is_pangram('The 123 brown foxes jump over the lazy dog!') == False
