
import pytest
from pytutils.excs import ok
from unittest.mock import patch

def test_valid_case_with_exception():
    with patch('builtins.print') as mock_print:
        try:
            with ok(ZeroDivisionError):
                print(1 / 0)  # This will not raise an error because ZeroDivisionError is passed.
        except Exception as e:
            pytest.fail("Unexpected exception was raised")
        
        assert mock_print.call_count == 0, "Print should not have been called"
