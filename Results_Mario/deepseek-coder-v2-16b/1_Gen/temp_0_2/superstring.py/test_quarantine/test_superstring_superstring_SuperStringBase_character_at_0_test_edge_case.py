
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperString

def test_character_at_edge_case():
    # Create a mock SuperString instance
    superstring_instance = MagicMock()
    superstring_instance.return_value.__getitem__.side_effect = lambda index: "Hello World"[index]
    
    # Call the character_at method with an edge case index (0)
    char = superstring_instance.character_at(0)
    
    # Assert that the returned character is 'h' after converting to lowercase
    assert char == "H".lower()

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_character_at_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________________________ test_character_at_edge_case __________________________

    def test_character_at_edge_case():
        # Create a mock SuperString instance
        superstring_instance = MagicMock()
        superstring_instance.return_value.__getitem__.side_effect = lambda index: "Hello World"[index]
    
        # Call the character_at method with an edge case index (0)
        char = superstring_instance.character_at(0)
    
        # Assert that the returned character is 'h' after converting to lowercase
>       assert char == "H".lower()
E       AssertionError: assert <MagicMock name='mock.character_at()' id='140140120217808'> == 'h'
E        +  where 'h' = <built-in method lower of str object at 0x7f74ec3a5408>()
E        +    where <built-in method lower of str object at 0x7f74ec3a5408> = 'H'.lower

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_character_at_0_test_edge_case.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_character_at_0_test_edge_case.py::test_character_at_edge_case
============================== 1 failed in 0.05s ===============================
"""