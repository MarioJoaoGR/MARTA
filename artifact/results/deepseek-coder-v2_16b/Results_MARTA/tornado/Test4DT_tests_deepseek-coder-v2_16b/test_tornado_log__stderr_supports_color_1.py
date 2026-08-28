
import pytest
import sys
try:
    import curses
except ImportError:
    curses = None
try:
    import colorama
except ImportError:
    colorama = None

def _stderr_supports_color() -> bool:
    try:
        if hasattr(sys.stderr, "isatty") and sys.stderr.isatty():
            if curses and curses.setupterm is not None:
                curses.setupterm()
                return curses.tigetnum("colors") > 0
            elif colorama:
                return sys.stderr is getattr(colorama.initialise, "wrapped_stderr", object())
    except Exception:
        pass
    return False

def test_stderr_supports_color():
    with pytest.raises(Exception):
        assert _stderr_supports_color() == True
