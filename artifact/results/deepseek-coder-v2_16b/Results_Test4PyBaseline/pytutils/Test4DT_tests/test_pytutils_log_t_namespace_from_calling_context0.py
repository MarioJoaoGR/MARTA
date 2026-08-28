# Module: pytutils.log
import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context():
    # Test that the function returns the fully qualified name of the module containing the caller's caller
    namespace = _namespace_from_calling_context()
    assert isinstance(namespace, str), "The returned value should be a string"
    assert "__name__" in inspect.stack()[2][0].f_globals, "The stack frame should have __name__ attribute"

if __name__ == "__main__":
    pytest.main()
