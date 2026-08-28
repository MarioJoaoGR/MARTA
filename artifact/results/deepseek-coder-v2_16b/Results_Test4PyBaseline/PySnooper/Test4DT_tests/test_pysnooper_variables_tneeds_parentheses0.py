
# Module: pysnooper.variables
# test_pysnooper_variables.py
from pysnooper.variables import needs_parentheses

def test_needs_parentheses():
    # Example 1: Without parentheses, 'a + b' is interpreted as a single term
    assert needs_parentheses('a + b') == True
    
    # Example 2: With parentheses, '(a + b)' is clearly defined
    assert needs_parentheses('(a + b)') == False
    
    # Example 3: Parentheses are necessary to form a complete if statement