# Module: pytutils.log
import pytest
import inspect
from pytutils.log import _namespace_from_calling_context

def test_namespace_from_calling_context():
    # Test that the function returns the fully qualified name of the module containing the caller's caller
    assert isinstance(_namespace_from_calling_context(), str), "The result should be a string"
    
    # Assuming this is run in a module named 'test_module', and test_module calls _namespace_from_calling_context
    expected_namespace = inspect.stack()[1][0].f_globals["__name__"]
    assert _namespace_from_calling_context() == expected_namespace, "The function should return the namespace of the caller's caller"

if __name__ == "__main__":
    pytest.main()
