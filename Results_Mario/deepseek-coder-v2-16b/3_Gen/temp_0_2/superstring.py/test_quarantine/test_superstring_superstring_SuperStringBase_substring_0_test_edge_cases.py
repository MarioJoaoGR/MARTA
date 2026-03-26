
import pytest
from superstring.superstring import SuperString, SuperStringSubstring, SUPERSTRING_MINIMAL_LENGTH

class SuperStringBase:
    def __init__(self, base=""):
        self._base = base

    def length(self):
        return len(self._base)

    def to_printable(self, start_index, end_index=None):
        if end_index is None:
            end_index = len(self._base)
        return self._base[start_index:end_index]

    def substring(self, start_index, end_index=None):
        """
        Extracts a substring from the current string starting at `start_index` and ending at `end_index`.
        
        Parameters:
            start_index (int): The index to begin the substring. If not provided, defaults to 0.
            end_index (int): The index to end the substring. If not provided, defaults to the length of the string.
        
        Returns:
            SuperString or SuperStringSubstring: A new instance of either `SuperString` or `SuperStringSubstring`, depending on the size of the extracted substring.
        
        Usage:
            ```python
            # Creating an instance of SuperStringBase with a base string and specified indices
            substr = SuperStringBase().substring(7, 12)
            
            # Accessing the attributes for debugging or further manipulation
            print(substr._base)      # Output: "Hello, World!" (if _base was set correctly)
            print(substr._start_index)  # Output: 7
            print(substr._end_index)    # Output: 12
            ```
        """
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        assert start_index < end_index, "Start index must be less than end index"
        if start_index == end_index:
            return SuperString("")
        if end_index - start_index <= SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.to_printable(start_index, end_index))
        return SuperStringSubstring(self._base, start_index, end_index)

def test_edge_cases():
    mockClass = SuperStringBase()
    
    # Test substring with default start and end indices
    substr1 = mockClass.substring(0, 5)
    assert isinstance(substr1, (SuperString, SuperStringSubstring)), "The result should be an instance of either SuperString or SuperStringSubstring"
    
    # Test substring with start index equal to end index (should return an empty string)
    substr2 = mockClass.substring(5, 5)
    assert substr2._base == "", "The substring should be an empty string"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        mockClass = SuperStringBase()
    
        # Test substring with default start and end indices
        substr1 = mockClass.substring(0, 5)
        assert isinstance(substr1, (SuperString, SuperStringSubstring)), "The result should be an instance of either SuperString or SuperStringSubstring"
    
        # Test substring with start index equal to end index (should return an empty string)
>       substr2 = mockClass.substring(5, 5)

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_edge_cases.py:56: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_superstring_superstring_SuperStringBase_substring_0_test_edge_cases.SuperStringBase object at 0x7f73f0163ad0>
start_index = 5, end_index = 5

    def substring(self, start_index, end_index=None):
        """
        Extracts a substring from the current string starting at `start_index` and ending at `end_index`.
    
        Parameters:
            start_index (int): The index to begin the substring. If not provided, defaults to 0.
            end_index (int): The index to end the substring. If not provided, defaults to the length of the string.
    
        Returns:
            SuperString or SuperStringSubstring: A new instance of either `SuperString` or `SuperStringSubstring`, depending on the size of the extracted substring.
    
        Usage:
            ```python
            # Creating an instance of SuperStringBase with a base string and specified indices
            substr = SuperStringBase().substring(7, 12)
    
            # Accessing the attributes for debugging or further manipulation
            print(substr._base)      # Output: "Hello, World!" (if _base was set correctly)
            print(substr._start_index)  # Output: 7
            print(substr._end_index)    # Output: 12
            ```
        """
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
>       assert start_index < end_index, "Start index must be less than end index"
E       AssertionError: Start index must be less than end index
E       assert 5 < 5

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_edge_cases.py:41: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_substring_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.05s ===============================
"""