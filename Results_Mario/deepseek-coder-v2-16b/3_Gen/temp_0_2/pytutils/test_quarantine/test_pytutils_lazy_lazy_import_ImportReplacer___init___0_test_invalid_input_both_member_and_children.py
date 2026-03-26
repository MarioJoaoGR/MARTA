
from pytutils.lazy.lazy_import import ScopeReplacer

class ImportReplacer(ScopeReplacer):
    """This class is designed to replace only a portion of an import list. It will replace itself with a module, and then make children entries also ImportReplacer objects. This supports 'import foo.bar.baz' syntax.

    Parameters:
        scope (dict): The scope that objects should be imported into. Typically this is globals().
        name (str): The variable name. Often this is the same as the module_path.
        module_path (list): A list for the fully specified module path ['bzrlib', 'foo', 'bar'].
        member (str, optional): The member inside the module to import, often None, indicating the module is being imported.
        children (dict, optional): Children entries to be imported later. This should be a map of children specifications. Example: 
            {'foo':(['bzrlib', 'foo'], None, {'bar':(['bzrlib', 'foo', 'bar'], None {})})}.

    Raises:
        ValueError: If both `member` and `children` are supplied.

    Examples:
        import foo => name='foo' module_path=['foo'], member=None, children={}
        import foo.bar => name='foo' module_path=['foo'], member=None, children={'bar':(['foo', 'bar'], None, {}}
        from foo import bar => name='bar' module_path=['foo'], member='bar'
        from foo import bar, baz would get translated into 2 imports. One for 'name=bar' and one for 'name=baz'.
    """
    def __init__(self, scope, name, module_path, member=None, children={}):
        """Upon request import 'module_path' as the name 'module_name'.
        When imported, prepare children to also be imported.

        :param scope: The scope that objects should be imported into.
            Typically this is globals()
        :param name: The variable name. Often this is the same as the
            module_path. 'bzrlib'
        :param module_path: A list for the fully specified module path
            ['bzrlib', 'foo', 'bar']
        :param member: The member inside the module to import, often this is
            None, indicating the module is being imported.
        :param children: Children entries to be imported later.
            This should be a map of children specifications.
            ::
            
                {'foo':(['bzrlib', 'foo'], None,
                    {'bar':(['bzrlib', 'foo', 'bar'], None {})})
                }

        Examples::

            import foo => name='foo' module_path='foo',
                          member=None, children={}
            import foo.bar => name='foo' module_path='foo', member=None,
                              children={'bar':(['foo', 'bar'], None, {}}
            from foo import bar => name='bar' module_path='foo', member='bar'
                                   children={}
            from foo import bar, baz would get translated into 2 import
            requests. On for 'name=bar' and one for 'name=baz'
        """
        if (member is not None) and children:
            raise ValueError('Cannot supply both a member and children')

        object.__setattr__(self, '_import_replacer_children', children)
        object.__setattr__(self, '_member', member)
        object.__setattr__(self, '_module_path', module_path)

        # Indirecting through __class__ so that children can
        # override _import (especially our instrumented version)
        cls = object.__getattribute__(self, '__class__')
        ScopeReplacer.__init__(self, scope=scope, name=name,
                               factory=cls._import)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.04s =============================
"""