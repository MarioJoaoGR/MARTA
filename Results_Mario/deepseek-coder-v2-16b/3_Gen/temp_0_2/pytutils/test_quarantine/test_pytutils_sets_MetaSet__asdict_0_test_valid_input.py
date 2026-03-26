
import pytest
from pytutils.sets import MetaSet
from datetime import datetime
import copy

@pytest.fixture
def meta_set():
    return MetaSet()

def test_valid_input(meta_set):
    # Add a valid value to the MetaSet and check if metadata is correctly updated
    initial_value = 'example_value'
    meta_set.add(initial_value)
    
    assert len(meta_set._store) == 1
    assert initial_value in meta_set._store
    assert len(meta_set._meta) == 1
    identifier = meta_set._meta_func(initial_value)
    assert meta_set._meta[identifier]['value'] == initial_value

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

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

meta_set = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f7ec763b600>, _store={'example_value'}, _meta={'example_value': 1}, _initial=None)

    def test_valid_input(meta_set):
        # Add a valid value to the MetaSet and check if metadata is correctly updated
        initial_value = 'example_value'
        meta_set.add(initial_value)
    
        assert len(meta_set._store) == 1
        assert initial_value in meta_set._store
        assert len(meta_set._meta) == 1
        identifier = meta_set._meta_func(initial_value)
>       assert meta_set._meta[identifier]['value'] == initial_value
E       KeyError: 0

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_input.py:20: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.08s ===============================
"""