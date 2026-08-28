
import pytest
from pymonet.monad_try import Try
from unittest.mock import patch

def test_get_or_else_success():
    try_success = Try(42, True)
    with patch('builtins.print') as mock_print:
        result = try_success.get_or_else("Default")
        assert result == 42
        mock_print.assert_not_called()
