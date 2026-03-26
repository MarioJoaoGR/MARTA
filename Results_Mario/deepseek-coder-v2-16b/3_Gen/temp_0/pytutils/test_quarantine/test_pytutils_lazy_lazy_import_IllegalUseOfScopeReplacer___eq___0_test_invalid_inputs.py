
from pytutils.lazy.lazy_import import LazyImport

class IllegalUseOfScopeReplacer:
    """
    A class to handle the reporting of incorrect usage of a ScopeReplacer object.

    This class is designed to be used when a ScopeReplacer object is misused. It provides a formatted error message that includes the name, message, and any extra information provided by the user.

    Parameters:
        name (str): The name associated with the misuse of the ScopeReplacer object. This helps in identifying which part of the code is using it incorrectly.
        msg (str): A descriptive error message that explains what went wrong when using the ScopeReplacer object.
        extra (optional, str or None): Additional information to include in the error message. If provided, this should be a string that supplements the main error message. Defaults to None.

    Example:
        >>> err = IllegalUseOfScopeReplacer('example_name', 'This is an example error message')
        >>> print(err._fmt % {'name': 'example_name', 'msg': 'This is an example error message', 'extra': ''})
        ScopeReplacer object 'example_name' was used incorrectly: This is an example error message

        >>> err = IllegalUseOfScopeReplacer('another_name', 'Another error occurred', extra='Additional details')
        >>> print(err._fmt % {'name': 'another_name', 'msg': 'Another error occurred', 'extra': ': Additional details'})
        ScopeReplacer object 'another_name' was used incorrectly: Another error occurred: Additional details

    Note:
        The function does not return any value. It is intended to be used for reporting errors in the usage of a ScopeReplacer object.
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
            bool: True if both objects are considered equal, False otherwise. If the classes do not match, returns NotImplemented.

        Usage:
            This method is used to determine if two instances of a class are equivalent by comparing their attribute dictionaries. It ensures that only instances of the same class can be compared and then checks if their attributes are identical.
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