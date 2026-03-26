
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

    def __repr__(self):
        """
        Generates a string representation of the object, including its class name and attribute values.

        This method is typically used to provide an unambiguous representation of the object for debugging purposes. It returns a string in the format `ClassName(attribute1=value1, attribute2=value2, ...)`.

        Parameters:
            None

        Returns:
            str: A string representing the object, including its class name and all attributes that can be represented as strings.

        Usage:
            obj = MyClass()
            print(obj.__repr__())  # Outputs: 'MyClass(attribute1=value1, attribute2=value2, ...)
        """
        return '%s(%s)' % (self.__class__.__name__, str(self))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_valid_inputs.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""