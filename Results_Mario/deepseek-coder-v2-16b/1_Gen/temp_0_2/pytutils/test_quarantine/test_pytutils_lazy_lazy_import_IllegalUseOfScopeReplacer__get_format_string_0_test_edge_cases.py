
from pytutils.lazy import lazy_import
from bzrlib.i18n import gettext

class IllegalUseOfScopeReplacer(Exception):
    """
    A custom exception class used to indicate that the ScopeReplacer object was used incorrectly.

    Parameters:
        name (str): The name associated with the error. This is a string representation of the name.
        msg (str): The error message explaining why the ScopeReplacer was used incorrectly.
        extra (optional, str): Additional information or context about the error. If provided, it will be concatenated to the error message with a colon and space.

    Raises:
        This class is intended for raising exceptions, so it does not return any value itself.

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
            lazy_import('bzrlib.i18n').gettext  # Lazy import to avoid immediate import error
            return gettext(unicode(fmt))  # _fmt strings should be ascii

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases.py:3:0: E0401: Unable to import 'bzrlib.i18n' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases.py:46:12: E1102: lazy_import is not callable (not-callable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_edge_cases.py:47:27: E0602: Undefined variable 'unicode' (undefined-variable)


"""