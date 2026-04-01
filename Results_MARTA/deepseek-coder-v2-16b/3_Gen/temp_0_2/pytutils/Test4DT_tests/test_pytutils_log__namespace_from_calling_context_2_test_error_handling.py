
import inspect
import pytest
from unittest.mock import patch

def _namespace_from_calling_context():
    """
    Derive a namespace from the module containing the caller's caller.

    :return: the fully qualified python name of a module.
    :rtype: str
    """
    # Not py3k compat
    # return inspect.currentframe(2).f_globals["__name__"]
    # TODO Does this work in both py2/3?
    return inspect.stack()[2][0].f_globals["__name__"]

def test_error_handling():
    with pytest.raises(IndexError):
        with patch('inspect.stack', return_value=[]):
            _namespace_from_calling_context()
