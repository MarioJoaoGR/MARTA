
import pytest
from unittest.mock import patch
import random
from pytutils.rand import rand_hex

@pytest.mark.parametrize("input_length, expected", [
    (8, True),
    (10, True),
    (5, True),
    (20, True),
])
def test_custom_length(input_length, expected):
    with patch('random.randrange') as mock_randrange:
        # Set the return value of randrange to always produce a valid hex character
        mock_randrange.return_value = 0x123456789abcdef

        result = rand_hex(input_length)
        assert len(result) == input_length

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py F [ 25%]
FF.                                                                      [100%]

=================================== FAILURES ===================================
__________________________ test_custom_length[8-True] __________________________

input_length = 8, expected = True

    @pytest.mark.parametrize("input_length, expected", [
        (8, True),
        (10, True),
        (5, True),
        (20, True),
    ])
    def test_custom_length(input_length, expected):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a valid hex character
            mock_randrange.return_value = 0x123456789abcdef
    
            result = rand_hex(input_length)
>           assert len(result) == input_length
E           AssertionError: assert 15 == 8
E            +  where 15 = len('123456789abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py:19: AssertionError
_________________________ test_custom_length[10-True] __________________________

input_length = 10, expected = True

    @pytest.mark.parametrize("input_length, expected", [
        (8, True),
        (10, True),
        (5, True),
        (20, True),
    ])
    def test_custom_length(input_length, expected):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a valid hex character
            mock_randrange.return_value = 0x123456789abcdef
    
            result = rand_hex(input_length)
>           assert len(result) == input_length
E           AssertionError: assert 15 == 10
E            +  where 15 = len('123456789abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py:19: AssertionError
__________________________ test_custom_length[5-True] __________________________

input_length = 5, expected = True

    @pytest.mark.parametrize("input_length, expected", [
        (8, True),
        (10, True),
        (5, True),
        (20, True),
    ])
    def test_custom_length(input_length, expected):
        with patch('random.randrange') as mock_randrange:
            # Set the return value of randrange to always produce a valid hex character
            mock_randrange.return_value = 0x123456789abcdef
    
            result = rand_hex(input_length)
>           assert len(result) == input_length
E           AssertionError: assert 15 == 5
E            +  where 15 = len('123456789abcdef')

pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py::test_custom_length[8-True]
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py::test_custom_length[10-True]
FAILED pytutils/Test4DT_tests/test_pytutils_rand_rand_hex_1_test_custom_length.py::test_custom_length[5-True]
========================= 3 failed, 1 passed in 0.06s ==========================
"""