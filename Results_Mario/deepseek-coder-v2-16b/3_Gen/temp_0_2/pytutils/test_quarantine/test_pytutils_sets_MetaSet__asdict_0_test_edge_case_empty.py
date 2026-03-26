
import pytest
from pytutils.sets import MetaSet
from datetime import datetime
import copy

class TestMetaSet:
    def setUp(self):
        self._meta_func = lambda value: f"id_{value}"
        self._store = set()
        self._meta = {}
        self._initial = None
        self.meta_set = MetaSet(
            _meta_func=self._meta_func,
            _store=self._store,
            _meta=self._meta,
            _initial=self._initial
        )
    
    def test_add(self):
        self.meta_set.add('example_value')
        assert len(self.meta_set._meta) == 1
        assert 'example_value' in self.meta_set._store
        assert self.meta_set._meta[f"id_example_value"]['value'] == 'example_value'
    
    def test_asdict(self):
        self.meta_set.add('example_value')
        meta_dict = self.meta_set._asdict()
        assert isinstance(meta_dict, dict)
        assert len(meta_dict) == 1
        assert list(meta_dict.keys())[0] == f"id_example_value"
    
    def test_discard(self):
        self.meta_set.add('example_value')
        self.meta_set.discard('example_value')
        assert len(self.meta_set._store) == 0
        assert f"id_example_value" not in self.meta_set._meta

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ TestMetaSet.test_add _____________________________

self = <Test4DT_tests.test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.TestMetaSet object at 0x7f0685a922d0>

    def test_add(self):
>       self.meta_set.add('example_value')
E       AttributeError: 'TestMetaSet' object has no attribute 'meta_set'

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py:21: AttributeError
___________________________ TestMetaSet.test_asdict ____________________________

self = <Test4DT_tests.test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.TestMetaSet object at 0x7f068447bbd0>

    def test_asdict(self):
>       self.meta_set.add('example_value')
E       AttributeError: 'TestMetaSet' object has no attribute 'meta_set'

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py:27: AttributeError
___________________________ TestMetaSet.test_discard ___________________________

self = <Test4DT_tests.test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.TestMetaSet object at 0x7f06844982d0>

    def test_discard(self):
>       self.meta_set.add('example_value')
E       AttributeError: 'TestMetaSet' object has no attribute 'meta_set'

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py:34: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py::TestMetaSet::test_add
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py::TestMetaSet::test_asdict
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_edge_case_empty.py::TestMetaSet::test_discard
============================== 3 failed in 0.07s ===============================
"""