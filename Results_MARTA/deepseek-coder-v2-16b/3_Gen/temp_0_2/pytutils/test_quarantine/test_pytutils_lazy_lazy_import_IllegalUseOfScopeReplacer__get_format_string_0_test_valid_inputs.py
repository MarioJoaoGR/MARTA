
from pytutils.lazy import lazy_import

class IllegalUseOfScopeReplacer(Exception):
    """
    Exception class used to signal incorrect usage of the ScopeReplacer object.

    This exception is raised when the ScopeReplacer object is used improperly. It takes three parameters: `name`, `msg`, and an optional `extra`. The function provides a detailed error message that includes the name, message, and any additional information provided.

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
    def __init__(self, name, msg, extra=None):
        self.name = name
        self.msg = msg
        if extra:
            self.extra = ': ' + str(extra)
        else:
            self.extra = ''

        super(IllegalUseOfScopeReplacer, self).__init__()

    @lazy_import('bzrlib.i18n', globals(), locals())
    def _get_format_string(self):
        """Return format string for this exception or None"""
        fmt = getattr(self, '_fmt', None)
        if fmt is not None:
            from bzrlib.i18n import gettext
            return gettext(unicode(fmt)) # _fmt strings should be ascii

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs.py:43:5: E1102: lazy_import is not callable (not-callable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs.py:48:12: E0401: Unable to import 'bzrlib.i18n' (import-error)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer__get_format_string_0_test_valid_inputs.py:49:27: E0602: Undefined variable 'unicode' (undefined-variable)


"""