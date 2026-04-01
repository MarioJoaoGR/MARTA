
class InvalidPattern:
    _fmt = 'Invalid pattern(s) found. %(msg)s'
    
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self._format()

    def _format(self):
        if self.msg is None:
            return 'Invalid pattern(s) found.'
        else:
            try:
                fmt = self._get_format_string()
                if fmt:
                    d = dict(self.__dict__)
                    s = fmt % d
                    # __str__() should always return a 'str' object
                    # never a 'unicode' object.
                    return str(s)
            except Exception as e:
                return 'Unprintable exception %s: dict=%r, error=%r' \
                    % (self.__class__.__name__, self.__dict__, e)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_regex_InvalidPattern___str___0_test_none_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_InvalidPattern___str___0_test_none_input.py:16:22: E1101: Instance of 'InvalidPattern' has no '_get_format_string' member (no-member)


"""