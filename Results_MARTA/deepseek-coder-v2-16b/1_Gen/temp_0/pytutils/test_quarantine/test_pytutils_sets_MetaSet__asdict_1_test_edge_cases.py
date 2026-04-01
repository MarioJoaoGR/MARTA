
import pytest
from pytutils.sets import MetaSet
import random
import copy

@pytest.fixture(scope="module")
def meta_set():
    ms = MetaSet()
    yield ms

def test_edge_cases(meta_set):
    # Add a value to the set
    initial_value = 10
    meta_set._store.add(initial_value)
    
    # Check that the metadata is correctly added
    assert len(meta_set._meta) == 1, "Metadata dictionary should have one entry"
    assert list(meta_set._meta.keys())[0] == initial_value, "The key in the metadata dictionary should be the value added to the set"
    
    # Check that the _asdict method returns a copy of the metadata dictionary
    meta_dict = meta_set._asdict()
    assert isinstance(meta_dict, dict), "_asdict should return a dictionary"
    assert len(meta_dict) == 1, "The returned dictionary from _asdict should have one entry"
    assert list(meta_dict.keys())[0] == initial_value, "The key in the returned dictionary should be the value added to the set"

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

meta_set = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f7e63a3a200>, _store={10}, _meta={}, _initial=None)

    def test_edge_cases(meta_set):
        # Add a value to the set
        initial_value = 10
        meta_set._store.add(initial_value)
    
        # Check that the metadata is correctly added
>       assert len(meta_set._meta) == 1, "Metadata dictionary should have one entry"
E       AssertionError: Metadata dictionary should have one entry
E       assert 0 == 1
E        +  where 0 = len({})
E        +    where {} = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f7e63a3a200>, _store={10}, _meta={}, _initial=None)._meta

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_1_test_edge_cases.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.06s ===============================
"""