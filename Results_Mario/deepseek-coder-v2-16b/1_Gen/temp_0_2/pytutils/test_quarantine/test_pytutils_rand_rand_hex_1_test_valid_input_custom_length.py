
import pytest
from unittest.mock import patch
from pytutils.rand import rand_hex

@pytest.mark.parametrize("length", [10])
def test_valid_input_custom_length(length):
    with patch('random.randrange') as mock_randrange:
        # Set the return value of randrange to always produce a hex string of the specified length
        mock_randrange.return_value = 0xabcdef1234567890  # This is an example value, adjust as necessary
        
        result = rand_hex(length)
        assert len(result) == length

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_valid_input_custom_length.py F [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_custom_length[10] ______________________

length = 10

    @pytest.mark.parametrize("length", [10])
    def test_valid_input_custom_length(length):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a hex string of the specified length
            mock_randrange.return_value = 0xabcdef1234567890  # This is an example value, adjust as necessary
    
            result = rand_hex(length)
>           assert len(result) == length
E           AssertionError: assert 16 == 10
E            +  where 16 = len('abcdef1234567890')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_valid_input_custom_length.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_valid_input_custom_length.py::test_valid_input_custom_length[10]
============================== 1 failed in 0.05s ===============================
"""