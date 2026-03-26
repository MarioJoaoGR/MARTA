
from pytutils.lazy.lazy_import import LazyImport

class ScopeReplacer:
    """A lazy object that will replace itself in the appropriate scope. This object sits, ready to create the real object the first time it is needed.
    
    Parameters:
        scope (dict): The scope where the placeholder should appear initially.
        factory (callable): A callable that will create the real object. It will be passed (self, scope, name).
        name (str): The variable name in the given scope to which the placeholder is bound.
    
    Example:
        >>> class MyObject: pass
        >>> scope = {}
        >>> factory = lambda self, s, n: MyObject()
        >>> replacer = ScopeReplacer(scope, factory, 'my_obj')
        >>> assert 'my_obj' not in scope  # The placeholder is initially bound to the real object.
        >>> obj = replacer._resolve()  # Creating the real object for the first time.
        >>> assert isinstance(obj, MyObject) and 'my_obj' in scope  # Now the real object is in the scope.
        
    Note:
        The `ScopeReplacer` class is designed to be used as a placeholder that will be replaced by a real object when first accessed. It initializes itself in the provided scope with the given name and factory for creating the real object. Once created, it ensures that subsequent accesses return the same real object unless proxying is disabled.
    
    Raises:
        IllegalUseOfScopeReplacer: If the proxy generation is disabled, or if the object attempted to replace itself during creation.
    """
    __slots__ = '_scope', '_factory', '_name', '_real_obj'
    _should_proxy = True
    
    def __init__(self, scope, factory, name):
        """Create a temporary object in the specified scope.
        Once used, a real object will be placed in the scope.

        :param scope: The scope the object should appear in
        :param factory: A callable that will create the real object.
            It will be passed (self, scope, name)
        :param name: The variable name in the given scope.
        """
        self._scope = scope
        self._factory = factory
        self._name = name
        self._real_obj = None
        scope[name] = self

    def _resolve(self):
        """Return the real object for which this is a placeholder"""
        if self._real_obj is None:
            # No obj generated previously, so generate from factory and scope.
            factory = self._factory
            scope = self._scope
            obj = factory(self, scope, self._name)
            if obj is self:
                raise IllegalUseOfScopeReplacer(self._name, msg="Object tried"
                    " to replace itself, check it's not using its own scope.")

            # Check if another thread has jumped in while obj was generated.
            if self._real_obj is None:
                # Still no prexisting obj, so go ahead and assign to scope and
                # return. There is still a small window here where races will
                # not be detected, but safest to avoid additional locking.
                self._real_obj = obj
                self._scope[self._name] = obj
                return obj

        # Raise if proxying is disabled as obj has already been generated.
        if not ScopeReplacer._should_proxy:
            raise IllegalUseOfScopeReplacer(
                self._name, msg="Object already replaced, did you assign it"
                                  " to another variable?")
        return self._real_obj

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0_test_valid_input.py:2:0: E0611: No name 'LazyImport' in module 'pytutils.lazy.lazy_import' (no-name-in-module)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0_test_valid_input.py:53:22: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ScopeReplacer__resolve_0_test_valid_input.py:67:18: E0602: Undefined variable 'IllegalUseOfScopeReplacer' (undefined-variable)


"""