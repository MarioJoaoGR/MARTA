
from unittest.mock import MagicMock
import pytest
from superstring.superstring import SuperStringUpper

def test_valid_input():
    # Create a mock instance of SuperStringBase
    base_string = MagicMock()
    base_string.character_at = MagicMock(side_effect=['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'])
    
    # Create an instance of SuperStringUpper with the mock base string
    upper_instance = SuperStringUpper(base_string)
    
    # Test valid indices
    assert upper_instance.character_at(0) == 'H'
    assert upper_instance.character_at(1) == 'E'
    assert upper_instance.character_at(7) == 'W'  # Corrected assertion to match the expected behavior

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Create a mock instance of SuperStringBase
        base_string = MagicMock()
        base_string.character_at = MagicMock(side_effect=['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'])
    
        # Create an instance of SuperStringUpper with the mock base string
        upper_instance = SuperStringUpper(base_string)
    
        # Test valid indices
        assert upper_instance.character_at(0) == 'H'
        assert upper_instance.character_at(1) == 'E'
>       assert upper_instance.character_at(7) == 'W'  # Corrected assertion to match the expected behavior
E       AssertionError: assert 'L' == 'W'
E         
E         - W
E         + L

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_0_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.05s ===============================
"""