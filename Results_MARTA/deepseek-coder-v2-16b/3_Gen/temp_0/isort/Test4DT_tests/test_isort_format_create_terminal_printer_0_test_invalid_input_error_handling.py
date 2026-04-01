
import sys
from unittest.mock import patch

import pytest

from isort.format import colorama_unavailable, create_terminal_printer


def test_invalid_input_error_handling():
    with patch('isort.format.colorama_unavailable', return_value=True):
        with pytest.raises(SystemExit) as e:
            # Test when color is True and colorama is unavailable
            create_terminal_printer(True, None, "Error message", "Success message")
    assert str(e.value) == '1'  # Check if the exit code is 1
