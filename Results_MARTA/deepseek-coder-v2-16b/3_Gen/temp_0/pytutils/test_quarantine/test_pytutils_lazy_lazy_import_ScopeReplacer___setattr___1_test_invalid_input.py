
from pytutils.lazy.lazy_import import LazyImport

class ScopeReplacer:
    """A lazy object that will replace itself in the appropriate scope. This object sits ready to create the real object the first time it is needed.
    
    Parameters:
        - `scope`: The scope the object should appear in. It should be a dictionary-like object where the real object will be placed once used.
        - `factory`: A callable that will create the real object. It will be passed (self, scope, name).
        - `name`: The variable name in the given scope.
    """
    __slots__ = '_scope', '_factory', '_name', '_real_obj'
    _should_proxy = True
    
    def __init__(self, scope, factory, name):
        """Create a temporary object in the specified scope. Once used, a real object will be placed in the scope.
        
        Parameters:
            - `scope`: The scope the object should appear in.
            - `factory`: A callable that will create the real object. It will be passed (self, scope, name).
            - `name`: The variable name in the given scope.
        """
        self._scope = scope
        self._factory = factory
        self._name = name
        self._real_obj = None
        scope[name] = self

    def __setattr__(self, attr, value):
        obj = self._resolve()
        return setattr(obj, attr, value)
    
    def _resolve(self):
        if self._real_obj is None:
            self._real_obj = self._factory(self, self._scope, self._name)
        return self._real_obj

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ScopeReplacer___setattr___1_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer___setattr___1_test_invalid_input.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)


"""