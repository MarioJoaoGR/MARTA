
from pytutils.lazy.lazy_import import LazyImport

class IllegalUseOfScopeReplacer:
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
        return '%s(%s)' % (self.__class__.__name__, str(self))

# Test case for the IllegalUseOfScopeReplacer class
def test_valid_input():
    err = IllegalUseOfScopeReplacer('example_name', 'This is an example error message.')
    assert repr(err) == "IllegalUseOfScopeReplacer('example_name', 'This is an example error message.', extra='')"
    
    err_with_extra = IllegalUseOfScopeReplacer('another_func', 'Argument missing.', extra='See documentation for details.')
    assert repr(err_with_extra) == "IllegalUseOfScopeReplacer('another_func', 'Argument missing.', extra=': See documentation for details')"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_valid_input.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""