
import pytest
from unittest.mock import patch
import inspect

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

def test_invalid_module():
    with patch('inspect.stack', side_effect=ImportError("Module not found")):
        with pytest.raises(ImportError):
            _namespace_from_calling_context()
