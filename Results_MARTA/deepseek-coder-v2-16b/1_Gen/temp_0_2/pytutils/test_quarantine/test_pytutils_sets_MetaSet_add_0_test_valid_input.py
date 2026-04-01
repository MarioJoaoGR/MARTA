
import pytest
from pytutils.sets import MetaSet

class MyMetaFunc:
    def __call__(self, value, **kwargs):
        return 0 if value == "initial" else 1

@pytest.fixture
def meta_set():
    return MetaSet(meta_func=MyMetaFunc())

def test_valid_input(meta_set):
    # Add initial value
    meta_set.add('initial')
    assert 'initial' in meta_set._store
    assert meta_set._meta['initial'] == 0

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet_add_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

meta_set = MetaSet(_meta_func=<Test4DT_tests.test_pytutils_sets_MetaSet_add_0_test_valid_input.MyMetaFunc object at 0x7f513fdb8bd0>, _store=set(), _meta={}, _initial=None)

    def test_valid_input(meta_set):
        # Add initial value
>       meta_set.add('initial')

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet_add_0_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = MetaSet(_meta_func=<Test4DT_tests.test_pytutils_sets_MetaSet_add_0_test_valid_input.MyMetaFunc object at 0x7f513fdb8bd0>, _store=set(), _meta={}, _initial=None)
value = 'initial'

    def add(self, value):
>       self._meta[value] = self._meta_func(value, self=self)
E       TypeError: MyMetaFunc.__call__() got multiple values for argument 'self'

pytutils/pytutils/sets.py:44: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet_add_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.06s ===============================
"""