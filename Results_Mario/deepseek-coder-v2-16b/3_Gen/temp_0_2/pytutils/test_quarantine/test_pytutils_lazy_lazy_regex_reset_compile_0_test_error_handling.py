
import re
from unittest.mock import patch, MagicMock
from pytutils.lazy.lazy_regex import reset_compile

def test_error_handling():
    with patch('builtins.__import__', side_effect=ImportError):
        with patch('pytutils.lazy.lazy_regex._real_re_compile', MagicMock()):
            try:
                reset_compile()
            except ImportError as e:
                assert str(e) == "No module named 're'"
