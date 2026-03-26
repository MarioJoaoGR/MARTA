
from pytutils.lazy.lazy_import import LazyImport

class IllegalUseOfScopeReplacer(Exception):
    """
    A class to handle the reporting of incorrect usage of a ScopeReplacer object.

    This class is designed to be used when a ScopeReplacer object is misused. It provides a formatted error message that includes details about how and why it was used incorrectly.

    Parameters:
        name (str): The name associated with the misuse, which will be included in the error message.
        msg (str): A brief description of what went wrong when using the ScopeReplacer object.
        extra (optional, str or None): Additional information that can be appended to the error message to provide more context. If provided, it should be a string; if not, this parameter is ignored.

    Attributes:
        name (str): The name associated with the misuse, which will be included in the error message.
        msg (str): A brief description of what went wrong when using the ScopeReplacer object.
        extra (str): Additional information that can be appended to the error message to provide more context. If not provided, this attribute is an empty string.

    Methods:
        __init__(self, name, msg, extra=None): Initializes the instance with the given parameters and sets up the error message format.

    Example Usage:
        >>> try:
        ...     scope_replacer = ScopeReplacer('example', 'This is an example of misuse.')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)  # Outputs: ScopeReplacer object 'example' was used incorrectly: This is an example of misuse.
        ...              # If extra information is provided, it will be appended to the message.
        >>> try:
        ...     scope_replacer = IllegalUseOfScopeReplacer('another_example', 'Another example of misuse.', 'Please check your inputs.')
        ... except IllegalUseOfScopeReplacer as e:
        ...     print(e)  # Outputs: ScopeReplacer object 'another_example' was used incorrectly: Another example of misuse.: Please check your inputs.
    """
    _fmt = 'ScopeReplacer object %(name)r was used incorrectly: %(msg)s%(extra)s'
    
    def __init__(self, name, msg, extra=None):
        self.name = name
        self.msg = msg
        if extra:
            self.extra = ': ' + str(extra)
        else:
            self.extra = ''

        super().__init__()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.msg}, extra={self.extra})'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_edge_cases
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_edge_cases.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""