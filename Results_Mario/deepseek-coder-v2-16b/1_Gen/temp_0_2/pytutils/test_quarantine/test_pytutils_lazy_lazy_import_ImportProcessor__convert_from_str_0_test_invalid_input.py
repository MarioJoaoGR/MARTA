
from pytutils.lazy import lazy_import
import pytest
from unittest.mock import patch, MagicMock

class ImportProcessor:
    """Convert text that users input into lazy import requests"""
    
    def __init__(self, lazy_import_class=None):
        """Initialize the ImportProcessor with an optional custom lazy import class.
        
        :param lazy_import_class: A class to be used for replacing imports (default is ImportReplacer)
        :type lazy_import_class: Optional[Type]
        """
        self.imports = {}
        if lazy_import_class is None:
            self._lazy_import_class = ImportReplacer
        else:
            self._lazy_import_class = lazy_import_class

    def _convert_from_str(self, from_str):
        """This converts a 'from foo import bar' string into an import map.

        :param from_str: The import string to process
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
                raise ImportNameCollision(name)
            self.imports[name] = (from_module_path, module, {})

class ImportReplacer:
    pass

class ImportNameCollision(Exception):
    pass

@pytest.fixture
def processor():
    return ImportProcessor()

@pytest.mark.parametrize("input_str", [
    "from os import path",
    "from sys import modules as mods",
    "from bzrlib import branch, transport"
])
def test_invalid_input(processor, input_str):
    with pytest.raises(ValueError):
        processor._convert_from_str(input_str)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________ test_invalid_input[from os import path] ____________________

processor = <Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.ImportProcessor object at 0x7f0450824b10>
input_str = 'from os import path'

    @pytest.mark.parametrize("input_str", [
        "from os import path",
        "from sys import modules as mods",
        "from bzrlib import branch, transport"
    ])
    def test_invalid_input(processor, input_str):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py:67: Failed
_____________ test_invalid_input[from sys import modules as mods] ______________

processor = <Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.ImportProcessor object at 0x7f0450b9cb50>
input_str = 'from sys import modules as mods'

    @pytest.mark.parametrize("input_str", [
        "from os import path",
        "from sys import modules as mods",
        "from bzrlib import branch, transport"
    ])
    def test_invalid_input(processor, input_str):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py:67: Failed
___________ test_invalid_input[from bzrlib import branch, transport] ___________

processor = <Test4DT_tests.test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.ImportProcessor object at 0x7f0450b9c650>
input_str = 'from bzrlib import branch, transport'

    @pytest.mark.parametrize("input_str", [
        "from os import path",
        "from sys import modules as mods",
        "from bzrlib import branch, transport"
    ])
    def test_invalid_input(processor, input_str):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py:67: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py::test_invalid_input[from os import path]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py::test_invalid_input[from sys import modules as mods]
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_0_test_invalid_input.py::test_invalid_input[from bzrlib import branch, transport]
============================== 3 failed in 0.07s ===============================
"""