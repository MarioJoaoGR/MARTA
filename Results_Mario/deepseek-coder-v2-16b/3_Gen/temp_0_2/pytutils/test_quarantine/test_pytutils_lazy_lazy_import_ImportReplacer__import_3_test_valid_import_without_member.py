
from pytutils.lazy.lazy_import import ImportReplacer

def test_valid_import_without_member():
    scope = {}
    name = 'foo'
    module_path = ['foo']
    member = None
    children = {}

    ir = ImportReplacer(scope, name, module_path, member, children)

    assert hasattr(ir, '_import_replacer_children')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_3_test_valid_import_without_member.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_import_without_member _______________________

    def test_valid_import_without_member():
        scope = {}
        name = 'foo'
        module_path = ['foo']
        member = None
        children = {}
    
        ir = ImportReplacer(scope, name, module_path, member, children)
    
>       assert hasattr(ir, '_import_replacer_children')

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_3_test_valid_import_without_member.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_import.py:182: in __getattribute__
    obj = object.__getattribute__(self, '_resolve')()
pytutils/pytutils/lazy/lazy_import.py:159: in _resolve
    obj = factory(self, scope, name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportReplacer object at 0x7fbb730dca00>
scope = {'foo': <pytutils.lazy.lazy_import.ImportReplacer object at 0x7fbb730dca00>}
name = 'foo'

    def _import(self, scope, name):
        children = object.__getattribute__(self, '_import_replacer_children')
        member = object.__getattribute__(self, '_member')
        module_path = object.__getattribute__(self, '_module_path')
        module_python_path = '.'.join(module_path)
        if member is not None:
            module = __import__(module_python_path, scope, scope, [member], level=0)
            return getattr(module, member)
        else:
>           module = __import__(module_python_path, scope, scope, [], level=0)
E           ModuleNotFoundError: No module named 'foo'

pytutils/pytutils/lazy/lazy_import.py:277: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_3_test_valid_import_without_member.py::test_valid_import_without_member
============================== 1 failed in 0.08s ===============================
"""