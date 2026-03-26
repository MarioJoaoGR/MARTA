
from pytutils.lazy.lazy_import import LazyImport

class IllegalUseOfScopeReplacer(Exception):
    """
    A custom exception class used to indicate that the ScopeReplacer object was used incorrectly.

    Parameters:
        name (str): The name associated with the error. This is a string representation of the name.
        msg (str): The error message explaining why the ScopeReplacer was used incorrectly.
        extra (optional, str): Additional information or context about the error. If provided, it should be a string that will be concatenated to the error message with a colon and space.

    Raises:
        This class is intended to be used for raising exceptions, so it does not return any value itself.

    Example Usage:
        >>> try:
        ...     raise IllegalUseOfScopeReplacer('ScopeReplacer', 'This is an error message')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)  # Output will be: ScopeReplacer object 'ScopeReplacer' was used incorrectly: This is an error message
        ...
        >>> try:
        ...     raise IllegalUseOfScopeReplacer('ScopeReplacer', 'Another error occurred', 'Extra information')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)  # Output will be: ScopeReplacer object 'ScopeReplacer' was used incorrectly: Another error occurred: Extra information
        ...

    Notes:
        The `extra` parameter is optional and can be omitted if no additional information is needed. The format string for the exception message includes placeholders for `name`, `msg`, and `extra`.
    """
    _format = 'ScopeReplacer object %(name)r was used incorrectly: %(msg)s%(extra)s'

    def __init__(self, name, msg, extra=None):
        self.name = name
        self.msg = msg
        if extra:
            self.extra = ': ' + str(extra)
        else:
            self.extra = ''

        super(IllegalUseOfScopeReplacer, self).__init__()

    def __str__(self):
        s = self._format % {
            'name': self.name,
            'msg': self.msg,
            'extra': self.extra
        }
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf8')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___str___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___str___0_test_valid_inputs.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""