
from pytutils.lazy import lazy_import

class ImportReplacer(ScopeReplacer):
    """This class is designed to replace only a portion of an import list. It will replace itself with a module and then make child entries also ImportReplacer objects. At present, this only supports 'import foo.bar.baz' syntax.
    
    Parameters:
        scope (dict): The dictionary where the imported module will be placed.
        name (str): The variable name under which the module should be accessible.
        module_path (list): A list of strings representing the path to the module in the Python import hierarchy.
        member (str, optional): The specific attribute or class within the module to import. Defaults to None.
        children (dict, optional): A dictionary defining further submodules to be imported. Each key-value pair should contain another nested dictionary with similar parameters.
    
    Raises:
        ValueError: If both a member and children are supplied.
    
    Returns:
        The imported module or the specified member of the module.
    
    Examples:
        import foo => name='foo' module_path='foo', member=None, children={}
        import foo.bar => name='foo' module_path='foo', member=None, children={'bar':(['foo', 'bar'], None, {}}
        from foo import bar => name='bar' module_path='foo', member='bar'
        from foo import bar, baz would get translated into 2 imports. One for 'name=bar' and one for 'name=baz'.
    """
    __slots__ = '_import_replacer_children', '_member', '_module_path'
    
    def __init__(self, scope, name, module_path, member=None, children={}):
        if (member is not None) and children:
            raise ValueError('Cannot supply both a member and children')

        object.__setattr__(self, '_import_replacer_children', children)
        object.__setattr__(self, '_member', member)
        object.__setattr__(self, '_module_path', module_path)

        # Indirecting through __class__ so that children can override _import (especially our instrumented version)
        cls = object.__getattribute__(self, '__class__')
        ScopeReplacer.__init__(self, scope=scope, name=name, factory=cls._import)

    @lazy_import
    def _import(self, scope, name):
        """Private method to perform the actual import of the module.
        
        Parameters:
            scope (dict): The dictionary where the imported module will be placed.
            name (str): The variable name under which the module should be accessible.
        
        Returns:
            The imported module, or a class if `member` is specified within the children definition.
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
            cls(module.__dict__, name=child_name, module_path=child_path, member=child_member, children=grandchildren)
        return module

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportReplacer__import_0_test_valid_input_happy_path
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_0_test_valid_input_happy_path.py:4:21: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_0_test_valid_input_happy_path.py:38:8: E0602: Undefined variable 'ScopeReplacer' (undefined-variable)


"""