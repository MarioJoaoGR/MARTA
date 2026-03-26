
from pytutils.lazy.lazy_import import ScopeReplacer

class ImportReplacer(ScopeReplacer):
    """This class is designed to replace only a portion of an import list. It will replace itself with a module, and then make child entries also ImportReplacer objects.
    
    Parameters:
        scope (dict): The scope that objects should be imported into. Typically this is globals().
        name (str): The variable name. Often this is the same as the module_path.
        module_path (list): A list for the fully specified module path ['bzrlib', 'foo', 'bar'].
        member (str, optional): The member inside the module to import, often None, indicating the module is being imported.
        children (dict, optional): Children entries to be imported later. This should be a map of children specifications.
        
    Examples:
        ImportReplacer(scope=globals(), name='foo', module_path=['foo']) will replace itself with 'foo' module and does not have any children.
        ImportReplacer(scope=globals(), name='foo', module_path=['foo'], member='bar') will import the member 'bar' from the module 'foo'.
        ImportReplacer(scope=globals(), name='foo', module_path=['foo'], children={'bar': (['foo', 'bar'], None, {})}) will replace itself with 'foo' and prepare to import 'bar' as a child.
    
    Raises:
        ValueError: If both `member` and `children` are supplied.
        
    Returns:
        None
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

    def _import(self, scope, name):
        """Private method to dynamically import modules and instantiate child classes.
        
        This function is used internally by the class to dynamically import modules based on the provided scope, name, module path, and children information. It handles both importing of modules with a specified member as well as direct imports without a specific member. After successful import, it instantiates any child classes defined in the `_import_replacer_children` attribute.
        
        Parameters:
            - scope (dict): The dictionary where the imported module will be placed.
            - name (str): The name of the module or class to be imported.
            
        Returns:
            The imported module or class, depending on whether a specific member was provided during import.
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
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-96w7aa8_'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-yflhb0fm'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================= 2 warnings in 0.04s ==============================
"""