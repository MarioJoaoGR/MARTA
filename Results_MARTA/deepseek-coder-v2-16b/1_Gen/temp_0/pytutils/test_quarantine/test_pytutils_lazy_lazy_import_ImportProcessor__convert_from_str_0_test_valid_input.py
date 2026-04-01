
from pytutils.lazy.lazy_import import ImportReplacer

class ImportProcessor:
    """Convert text that users input into lazy import requests.

    This class provides functionality to replace standard imports with a custom lazy import mechanism, which can be specified during initialization or defaulting to ImportReplacer if not provided. The `imports` attribute is used to store the mappings of original imports to their replacements.

    Parameters:
        - lazy_import_class (optional): A class representing the lazy import mechanism to be used instead of the default ImportReplacer. If not provided, the default ImportReplacer will be used.

    Attributes:
        - imports (dict): A dictionary storing the mappings of original imports to their replacement classes or functions.
        - _lazy_import_class (ImportReplacer or custom class): The lazy import mechanism class that is currently in use, which can either be ImportReplacer or a user-defined subclass.

    Example:
        To create an instance of ImportProcessor using the default ImportReplacer:
        ```python
        processor = ImportProcessor()
        ```
        
        To create an instance with a custom lazy import class, say MyLazyImportClass:
        ```python
        processor = ImportProcessor(lazy_import_class=MyLazyImportClass)
        ```

    Raises:
        - TypeError: If the provided `lazy_import_class` is not a subclass of the base ImportReplacer.
    """
    
    def __init__(self, lazy_import_class=None):
        """Initialize the ImportProcessor with an optional custom lazy import class.
        
        :param lazy_import_class: A class to use for replacing imports, defaults to ImportReplacer if None is provided.
        :type lazy_import_class: Optional[Callable], optional
        """
        self.imports = {}
        if lazy_import_class is None:
            self._lazy_import_class = ImportReplacer
        else:
            self._lazy_import_class = lazy_import_class

    def _convert_from_str(self, from_str):
        """This converts a 'from foo import bar' string into an import map.
        
        :param from_str: The import string to process
        :raises ValueError: If the input string does not start with 'from ', raises a ValueError.
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
                raise errors.ImportNameCollision(name)
            self.imports[name] = (from_module_path, module, {})

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_valid_input.py:71:22: E0602: Undefined variable 'errors' (undefined-variable)


"""