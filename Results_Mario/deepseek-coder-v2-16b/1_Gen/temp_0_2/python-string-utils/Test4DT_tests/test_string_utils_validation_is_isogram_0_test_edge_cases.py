
from string_utils.validation import is_isogram

def test_edge_cases():
    # Test an empty string
    assert is_isogram('') == False, "Test failed for empty string"
    
    # Test a single character string
    assert is_isogram('a') == True, "Test failed for single character string 'a'"
    
    # Test a string with spaces
    assert is_isogram('dermatoglyphics') == True, "Test failed for string with no duplicate letters: 'dermatoglyphics'"
    
    # Test a string with spaces and hyphens
    assert is_isogram('subdermatoglyphic') == True, "Test failed for string with spaces and hyphens: 'subdermatoglyphic'"
    
    # Test a string with duplicate letters
    assert is_isogram('hello') == False, "Test failed for string with duplicate letters: 'hello'"
    
    # Test a string with mixed case but no duplicates
    assert is_isogram('Dermatoglyphics') == True, "Test failed for string with mixed case but no duplicates: 'Dermatoglyphics'"
    
    print("All test cases passed!")
