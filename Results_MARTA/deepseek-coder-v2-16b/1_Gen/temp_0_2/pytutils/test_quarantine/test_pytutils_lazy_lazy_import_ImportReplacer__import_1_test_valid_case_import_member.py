
from pytutils.lazy.lazy_import import lazy_import

class ImportReplacer(ScopeReplacer):
    """This class is designed to replace only a portion of an import list. It will replace itself with a module and then make child entries also ImportReplacer objects. At present, this only supports 'import foo.bar.baz' syntax.
    
    Parameters:
        scope (dict): The scope that objects should be imported into. Typically this is globals().
        name (str): The variable name. Often this is the same as the module_path.
        module_path (list): A list for the fully specified module path ['bzrlib', 'foo', 'bar'].
        member (str, optional): The member inside the module to import, often this is None, indicating the module is being imported.
        children (dict, optional): Children entries to be imported later. This should be a map of children specifications.
            {'foo':(['bzrlib', 'foo'], None, {'bar':(['bzrlib', 'foo', 'bar'], None {})})}.
    
    Raises:
        ValueError: If both a member and children are supplied.
    
    Examples:
        import foo => name='foo' module_path='foo', member=None, children={}
        import foo.bar => name='foo' module_path='foo', member=None, children={'bar':(['foo', 'bar'], None, {}}
        from foo import bar => name='bar' module_path='foo', member='bar'
        from foo import bar, baz would get translated into 2 imports. One for 'name=bar' and one for 'name=baz'.
    
    Returns:
        The imported module or the specified member of the module.
    """
    __slots__ = '_import_replacer_children', '_member', '_module_path'
    
    def __init__(self, scope, name, module_path, member=None, children={}):
        if (member is not None) and children:
            raise ValueError('Cannot supply both a member and children')

        object.__setattr__(self, '_import_replacer_children', children)
        object.__setattr__(self, '_member', member)
        object.__setattr__(self, '_module_path', module_path)

        cls = object.__getattribute__(self, '__class__')
        ScopeReplacer.__init__(self, scope=scope, name=name, factory=cls._import)

    @lazy_import
    def _import(self, scope, name):
        """Private method to dynamically import modules and instantiate child objects.
        
        This function is used internally by the class to manage the dynamic loading of modules and their members based on configuration. It allows for the injection of specific scopes, names, and paths to facilitate the importing and instantiation of nested modules or classes. The function ensures that children are also instantiated according to the provided configuration.
        
        Parameters:
            scope (dict): A dictionary representing the local namespace into which the module name is imported.
            name (str): The name under which the module should be accessible within the given scope.
        
        Returns:
            The imported module or class, if successfully loaded and instantiated.
        """
        children = object.__getattribute__(self, '_import_replacer_children')
        member = object.__getattribute__(self, '_member')
        module_path = object.__getattribute__(self, '_module_path')
        module_python_path = '.'.join(module_path)
        if member is not None:
            module = __import__(module_python_path, scope, scope, [member], level=0)
            return getattr(module, member)
        else:
            module = __import__(module_python_path, scope, scope, [], level=0)
            for path in module_path[1:]:
                module = getattr(module, path)

        # Prepare the children to be imported
        for child_name, (child_path, child_member, grandchildren) in \
                children.items():
            cls = object.__getattribute__(self, '__class__')
            cls(scope=scope, name=child_name, module_path=child_path, member=child_member, children=grandchildren)
        return module

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportReplacer__import_1_test_valid_case_import_member
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_1_test_valid_case_import_member.py:4:21: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_1_test_valid_case_import_member.py:38:8: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)


"""