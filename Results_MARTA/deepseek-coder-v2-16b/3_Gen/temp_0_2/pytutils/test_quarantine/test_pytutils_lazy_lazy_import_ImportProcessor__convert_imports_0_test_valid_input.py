
from pytutils.lazy import lazy_import

class ImportProcessor:
    """Convert text that users input into lazy import requests"""
    __slots__ = ['imports', '_lazy_import_class']

    def __init__(self, lazy_import_class=None):
        self.imports = {}
        if lazy_import_class is None:
            self._lazy_import_class = ImportReplacer
        else:
            self._lazy_import_class = lazy_import_class

    def _convert_imports(self, scope):
        # Now convert the map into a set of imports
        for name, info in self.imports.items():
            module_path, member, children = info
            self._lazy_import_class(scope, name=name, module_path=module_path,
                                    member=member, children=children)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0_test_valid_input
pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_0_test_valid_input.py:11:38: E0602: Undefined variable 'ImportReplacer' (undefined-variable)


"""