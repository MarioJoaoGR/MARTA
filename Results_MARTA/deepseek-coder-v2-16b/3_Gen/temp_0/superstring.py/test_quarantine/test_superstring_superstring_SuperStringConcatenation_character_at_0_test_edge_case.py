
from superstring.superstring import SuperStringConcatenation, SuperStringSubstring

def test_edge_case():
    # Create instances of SuperStringSubstring for both left and right substrings
    left_substr = SuperStringSubstring("Hello", 0, 5)
    right_substr = SuperStringSubstring("World!", 0, 5)
    
    # Initialize the concatenated object with these substrings
    concatenated = SuperStringConcatenation(left_substr, right_substr)
    
    # Test the character at index 0 (edge case for concatenation)
    assert concatenated.character_at(0) == 'H'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Create instances of SuperStringSubstring for both left and right substrings
        left_substr = SuperStringSubstring("Hello", 0, 5)
        right_substr = SuperStringSubstring("World!", 0, 5)
    
        # Initialize the concatenated object with these substrings
        concatenated = SuperStringConcatenation(left_substr, right_substr)
    
        # Test the character at index 0 (edge case for concatenation)
>       assert concatenated.character_at(0) == 'H'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
superstring.py/superstring/superstring.py:105: in character_at
    return self._left[index]
superstring.py/superstring/superstring.py:73: in __getitem__
    return self.character_at(key)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringSubstring object at 0x7f73d7ab9350>
index = 0

    def character_at(self, index):
>       return self._base.character_at(self._start_index + index)
E       AttributeError: 'str' object has no attribute 'character_at'

superstring.py/superstring/superstring.py:130: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.05s ===============================
"""