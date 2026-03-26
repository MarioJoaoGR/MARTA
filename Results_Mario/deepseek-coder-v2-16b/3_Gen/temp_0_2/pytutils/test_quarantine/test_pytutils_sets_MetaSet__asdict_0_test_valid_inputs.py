
import pytest
from pytutils.sets import MetaSet
from datetime import datetime
import copy

@pytest.fixture
def meta_set():
    return MetaSet()

def test_add(meta_set):
    value = 'example_value'
    meta_set.add(value)
    assert value in meta_set._store
    assert len(meta_set._meta) == 1
    identifier = meta_set._meta_func(value)
    assert meta_set._meta[identifier]['value'] == value

def test_asdict(meta_set):
    value = 'example_value'
    meta_set.add(value)
    meta_dict = meta_set._asdict()
    assert isinstance(meta_dict, dict)
    assert len(meta_dict) == 1
    key = next(iter(meta_dict))
    assert meta_dict[key]['value'] == value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_inputs.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________________ test_add ___________________________________

meta_set = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f5de769f9c0>, _store={'example_value'}, _meta={'example_value': 0}, _initial=None)

    def test_add(meta_set):
        value = 'example_value'
        meta_set.add(value)
        assert value in meta_set._store
        assert len(meta_set._meta) == 1
        identifier = meta_set._meta_func(value)
>       assert meta_set._meta[identifier]['value'] == value
E       KeyError: 0

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_inputs.py:17: KeyError
_________________________________ test_asdict __________________________________

meta_set = MetaSet(_meta_func=<function MetaSet.<lambda> at 0x7f5de769f9c0>, _store={'example_value'}, _meta={'example_value': 1}, _initial=None)

    def test_asdict(meta_set):
        value = 'example_value'
        meta_set.add(value)
        meta_dict = meta_set._asdict()
        assert isinstance(meta_dict, dict)
        assert len(meta_dict) == 1
        key = next(iter(meta_dict))
>       assert meta_dict[key]['value'] == value
E       TypeError: 'int' object is not subscriptable

pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_inputs.py:26: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_inputs.py::test_add
FAILED pytutils/Test4DT_tests/test_pytutils_sets_MetaSet__asdict_0_test_valid_inputs.py::test_asdict
============================== 2 failed in 0.09s ===============================
"""