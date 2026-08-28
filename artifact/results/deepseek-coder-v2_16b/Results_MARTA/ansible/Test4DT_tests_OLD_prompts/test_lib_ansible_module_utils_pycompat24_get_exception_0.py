
import pytest
from unittest.mock import patch
import sys

def get_exception():
    """Get the current exception.

    This code needs to work on Python 2.4 through 3.x, so we cannot use
    "except Exception, e:" (SyntaxError on Python 3.x) nor
    "except Exception as e:" (SyntaxError on Python 2.4-2.5).
    Instead we must use ::

        except Exception:
            e = get_exception()

    """
    return sys.exc_info()[1]


def test_invalid_input():
    with pytest.raises(TypeError):
        raise TypeError("This is a TypeError")