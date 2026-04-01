
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

    def _format(self):
        s = getattr(self, '_preformatted_string', None)
        if s is not None:
            # contains a preformatted message
            return s
        try:
            fmt = self._get_format_string()
            if fmt:
                d = dict(self.__dict__)
                s = fmt % d
                # __str__() should always return a 'str' object
                # never a 'unicode' object.
                return s
        except Exception as e:
            pass # just bind to 'e' for formatting below
        else:
            e = None
        return 'Unprintable exception %s: dict=%r, fmt=%r, error=%r' \
            % (self.__class__.__name__,
               self.__dict__,
               getattr(self, '_fmt', None),
               e)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_edge_cases.py:2:0: E0611: No name 'lazy_module' in module 'pytutils.lazy.lazy_import' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__format_0_test_edge_cases.py:52:18: E1101: Instance of 'IllegalUseOfScopeReplacer' has no '_get_format_string' member (no-member)


"""