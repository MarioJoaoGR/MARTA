
from pytutils.lazy.lazy_import import LazyImport

class IllegalUseOfScopeReplacer(Exception):
    """
    A class representing an error that occurs when a ScopeReplacer object is used incorrectly. This class initializes with the name of the object, 
    a message describing the issue, and optional extra information to include in the error message. The `__init__` method is defined twice in the provided code, 
    which is incorrect and redundant. Typically, you would define only one `__init__` method to avoid this issue.

    Parameters:
        name (str): The name of the object that was used incorrectly.
        msg (str): A message explaining what went wrong when using the object.
        extra (optional, str or None): Additional information to include in the error message. If provided, it should be a string; if not, this parameter can be omitted.

    Attributes:
        name (str): The name of the object that was used incorrectly.
        msg (str): A message explaining what went wrong when using the object.
        extra (str): Additional information to include in the error message, formatted as a string if provided.

    Example Usage:
        >>> err = IllegalUseOfScopeReplacer('example_name', 'This is an example error message.')
        >>> print(err._fmt % {'name': err.name, 'msg': err.msg, 'extra': err.extra})
        ScopeReplacer object 'example_name' was used incorrectly: This is an example error message.

    Raises:
        IllegalUseOfScopeReplacer: If the proxy mechanism is disabled and a replacement has already occurred.
    """
    _fmt = 'ScopeReplacer object %(name)r was used incorrectly: %(msg)s%(extra)s'
    
    def __init__(self, name, msg, extra=None):
        self.name = name
        self.msg = msg
        if extra:
            self.extra = ': ' + str(extra)
        else:
            self.extra = ''

        super(IllegalUseOfScopeReplacer, self).__init__()

    def __eq__(self, other):
        """
        Compares two objects for equality by comparing their dictionary representations of attributes.
        
        Parameters:
            other (object): The object to compare with the current instance.
        
        Returns:
            bool: True if both objects are considered equal, False otherwise. If the classes of the objects are different, returns NotImplemented.
        
        Usage:
            This method is typically used for comparing instances of classes where equality should be based on attribute values rather than identity. It allows comparison between objects of the same class or type.
        """
        if self.__class__ is not other.__class__:
            return NotImplemented
        return self.__dict__ == other.__dict__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___eq___0_test_invalid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___eq___0_test_invalid_inputs.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""