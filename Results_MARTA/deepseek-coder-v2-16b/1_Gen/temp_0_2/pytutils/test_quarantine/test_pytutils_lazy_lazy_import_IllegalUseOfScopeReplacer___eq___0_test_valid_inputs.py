
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
    
    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        return self.__dict__ == other.__dict__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___eq___0_test_valid_inputs
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_IllegalUseOfScopeReplacer___eq___0_test_valid_inputs.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""