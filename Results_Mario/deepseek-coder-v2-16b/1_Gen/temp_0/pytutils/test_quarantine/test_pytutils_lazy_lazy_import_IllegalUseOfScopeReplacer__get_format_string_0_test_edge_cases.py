
from pytutils.lazy import lazy_import
from bzrlib.i18n import gettext

class IllegalUseOfScopeReplacer(Exception):
    """
    A custom exception class used to indicate that the ScopeReplacer object was used incorrectly.

    Parameters:
        name (str): The name associated with the error. This is a string representation of the name.
        msg (str): The message explaining the reason for the error.
        extra (optional, str): Additional information to include in the exception message. If provided, it should be a string.

    Raises:
        IllegalUseOfScopeReplacer: This exception is raised when the ScopeReplacer object is used improperly.

    Example Usage:
        >>> try:
        ...     raise IllegalUseOfScopeReplacer('ScopeReplacer', 'This is an error message')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)
        ScopeReplacer object 'ScopeReplacer' was used incorrectly: This is an error message

    Notes:
        The `extra` parameter is optional and can be used to provide additional context or information about the error. If provided, it should be a string that will be appended to the main error message with a colon and space.
    
    Implementation Details:
        This class is designed to raise an exception when the ScopeReplacer object is misused. The constructor initializes the exception with a name, a message, and optional extra information. The `_get_format_string` method attempts to return a format string for the exception, which includes translation if available.
    """
    
    def __init__(self, name, msg, extra=None):
        self.name = name
        self.msg = msg
        if extra:
            self.extra = ': ' + str(extra)
        else:
            self.extra = ''

        super(IllegalUseOfScopeReplacer, self).__init__()

    def _get_format_string(self):
        """Return format string for this exception or None"""
        fmt = getattr(self, '_fmt', None)
        if fmt is not None:
            lazy_import('bzrlib.i18n').gettext  # Import gettext from bzrlib.i18n lazily
            return gettext(unicode(fmt))  # _fmt strings should be ascii

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases.py:3:0: E0401: Unable to import 'bzrlib.i18n' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases.py:45:12: E1102: lazy_import is not callable (not-callable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases.py:46:27: E0602: Undefined variable 'unicode' (undefined-variable)


"""