
import pytest
from unittest.mock import patch
from ansible.plugins.action.pause import is_interactive


def test_non_interactive_case():
    with patch('sys.stdin.isatty', return_value=False), \
         patch('os.getpgrp', return_value=12345):
        result = is_interactive(0)
        assert result is False, "Expected non-interactive process but got interactive"