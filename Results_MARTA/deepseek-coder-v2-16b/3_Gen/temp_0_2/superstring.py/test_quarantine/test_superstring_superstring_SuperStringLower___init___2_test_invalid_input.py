
import pytest
from superstring.superstring import SuperStringLower

def test_invalid_input():
    """
    This function tests the initialization of SuperStringLower with an invalid input to ensure it handles it correctly.
    
    Parameters:
    - base (str): The initial string that will be used as a basis for further operations. It is expected to be in uppercase.
    
    Returns:
        None
    """
    # Test case where the input is not a string
    with pytest.raises(TypeError) as excinfo:
        SuperStringLower(12345)  # Providing an integer instead of a string
    assert "base must be a str" in str(excinfo.value)
    
    # Test case where the input is None
    with pytest.raises(TypeError) as excinfo:
        SuperStringLower(None)  # Providing None instead of a string
    assert "base must be a str" in str(excinfo.value)

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower___init___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        """
        This function tests the initialization of SuperStringLower with an invalid input to ensure it handles it correctly.
    
        Parameters:
        - base (str): The initial string that will be used as a basis for further operations. It is expected to be in uppercase.
    
        Returns:
            None
        """
        # Test case where the input is not a string
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower___init___2_test_invalid_input.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower___init___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""