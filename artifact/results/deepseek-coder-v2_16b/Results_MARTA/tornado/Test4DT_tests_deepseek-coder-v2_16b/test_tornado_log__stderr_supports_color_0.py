
import pytest
from unittest.mock import patch
import sys

def _stderr_supports_color() -> bool:
    try:
        if hasattr(sys.stderr, "isatty") and sys.stderr.isatty():
            if 'curses' in sys.modules:
                import curses
                try:
                    curses.setupterm()
                    return curses.tigetnum("colors") > 0
                except Exception:
                    pass
            elif 'colorama' in sys.modules:
                from colorama import init
                init(wrap=False)
                return True
    except Exception:
        pass
    return False

@pytest.mark.skipif('curses' not in sys.modules and 'colorama' not in sys.modules, reason="Requires curses or colorama library")
def test_valid_case():
    with patch('sys.stderr.isatty', return_value=True):
        if 'curses' in sys.modules:
            import curses
            with patch('curses.setupterm', return_value=None):
                assert _stderr_supports_color() == True
        elif 'colorama' in sys.modules:
            from colorama import init
            init(wrap=False)
            assert _stderr_supports_color() == True
