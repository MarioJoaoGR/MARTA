
from pytutils.lazy.lazy_import import lazy_import

class ImportProcessor:
    """Convert text that users input into lazy import requests"""
    __slots__ = ['imports', '_lazy_import_class']
    
    def __init__(self, lazy_import_class=None):
        self.imports = {}
        if lazy_import_class is None:
            self._lazy_import_class = ImportReplacer
        else:
            self._lazy_import_class = lazy_import_class

    def _convert_import_str(self, import_str):
        """This converts a import string into an import map.

        This only understands 'import foo, foo.bar, foo.bar.baz as bing'

        :param import_str: The import string to process
        :raises ValueError: If the import string is not properly formatted
        """
        if not import_str.startswith('import '):
            raise ValueError('bad import string %r' % (import_str,))
        import_str = import_str[len('import '):]

        for path in import_str.split(','):
            path = path.strip()
            if not path:
                continue
            as_hunks = path.split(' as ')
            if len(as_hunks) == 2:
                # We have 'as' so this is a different style of import
                # 'import foo.bar.baz as bing' creates a local variable
                # named 'bing' which points to 'foo.bar.baz'
                name = as_hunks[1].strip()
                module_path = as_hunks[0].strip().split('.')
                if name in self.imports:
                    raise errors.ImportNameCollision(name)
                # No children available in 'import foo as bar'
                self.imports[name] = (module_path, None, {})
            else:
                # Now we need to handle
                module_path = path.split('.')
                name = module_path[0]
                if name not in self.imports:
                    # This is a new import that we haven't seen before
                    module_def = ([name], None, {})
                    self.imports[name] = module_def
                else:
                    module_def = self.imports[name]

                cur_path = [name]
                cur = module_def[2]
                for child in module_path[1:]:
                    cur_path.append(child)
                    if child in cur:
                        cur = cur[child][2]
                    else:
                        next = (cur_path[:], None, {})
                        cur[child] = next
                        cur = next[2]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_3_test_edge_case
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_3_test_edge_case.py:11:38: E0602: Undefined variable 'ImportReplacer' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_import_str_3_test_edge_case.py:39:26: E0602: Undefined variable 'errors' (undefined-variable)


"""