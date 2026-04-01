
from pytutils.lazy.lazy_import import lazy_module

@lazy_module(globals())
class IllegalUseOfScopeReplacer(Exception):
    """
    Exception class used to signal incorrect usage of the ScopeReplacer object.

    This exception is raised when the ScopeReplacer object is used improperly. It takes three parameters: `name`, `msg`, and an optional `extra`.

    Parameters:
        name (str): A string representing the name associated with the error.
        msg (str): A string message describing the error in more detail.
        extra (optional, str): Additional information about the error, which can be provided as a string. If not provided, it defaults to an empty string.

    Attributes:
        name (str): The name associated with the error.
        msg (str): A detailed message describing the error.
        extra (str): Optional additional information about the error.

    Example Usage:
        >>> try:
        ...     scope_replacer = ScopeReplacer('example', 'This is an example error')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)
        ScopeReplacer object 'example' was used incorrectly: This is an example error

        >>> try:
        ...     scope_replacer = ScopeReplacer('another_example', 'Another error occurred', 'Details: invalid operation')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)
        ScopeReplacer object 'another_example' was used incorrectly: Another error occurred: Details: invalid operation
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

    def __str__(self):
        s = self._format()
        if isinstance(s, unicode):
            s = s.encode('utf8')
        else:
            # __str__ must return a str.
            s = str(s)
        return s

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___str___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___str___0_test_valid_inputs.py:2:0: E0611: No name 'lazy_module' in module 'pytutils.lazy.lazy_import' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___str___0_test_valid_inputs.py:47:12: E1101: Instance of 'IllegalUseOfScopeReplacer' has no '_format' member (no-member)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___str___0_test_valid_inputs.py:48:25: E0602: Undefined variable 'unicode' (undefined-variable)


"""