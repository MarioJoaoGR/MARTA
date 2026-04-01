
from pytutils.lazy.lazy_import import ImportReplacer
import pytest

class ImportProcessor:
    """Convert text that users input into lazy import requests"""
    __slots__ = ['imports', '_lazy_import_class']
    
    def __init__(self, lazy_import_class=None):
        self.imports = {}
        if lazy_import_class is None:
            self._lazy_import_class = ImportReplacer
        else:
            self._lazy_import_class = lazy_import_class

    def _convert_from_str(self, from_str):
        """This converts a 'from foo import bar' string into an import map.
        
        :param from_str: The import string to process
        :raises ValueError: If the input string does not start with 'from ', it raises a ValueError.
        """
        if not from_str.startswith('from '):
            raise ValueError('bad from/import %r' % from_str)
        from_str = from_str[len('from '):]

        from_module, import_list = from_str.split(' import ')

        from_module_path = from_module.split('.')

        for path in import_list.split(','):
            path = path.strip()
            if not path:
                continue
            as_hunks = path.split(' as ')
            if len(as_hunks) == 2:
                # We have 'as' so this is a different style of import
                # 'import foo.bar.baz as bing' creates a local variable
                # named 'bing' which points to 'foo.bar.baz'
                name = as_hunks[1].strip()
                module = as_hunks[0].strip()
            else:
                name = module = path
            if name in self.imports:
                raise ValueError(f"Import name collision for {name}")
            self.imports[name] = (from_module_path, module, {})

def test_valid_input():
    processor = ImportProcessor()
    from_str = 'from foo import bar'
    processor._convert_from_str(from_str)
    assert len(processor.imports) == 1
    assert 'bar' in processor.imports
