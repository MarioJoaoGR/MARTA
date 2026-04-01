
from pytutils.lazy.lazy_import import LazyImport

class IllegalUseOfScopeReplacer(Exception):
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
        return '%s(%r, %r, extra=%r)' % (self.__class__.__name__, self.name, self.msg, self.extra)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___repr___0_test_invalid_input.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""