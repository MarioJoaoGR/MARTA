
import pytest
from flutes.multiproc import FuncWrapper

def add(a, b):
    return a + b

@pytest.mark.parametrize("fn, args, kwds", [
    (None, [], {}),
    (add, None, {}),
    (add, [], None),
    (None, None, None)
])
def test_edge_cases(fn, args, kwds):
    with pytest.raises(TypeError):
        FuncWrapper(fn, args, kwds)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
______________________ test_edge_cases[None-args0-kwds0] _______________________

fn = None, args = [], kwds = {}

    @pytest.mark.parametrize("fn, args, kwds", [
        (None, [], {}),
        (add, None, {}),
        (add, [], None),
        (None, None, None)
    ])
    def test_edge_cases(fn, args, kwds):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py:15: Failed
_______________________ test_edge_cases[add-None-kwds1] ________________________

fn = <function add at 0x7f6c35a5bb00>, args = None, kwds = {}

    @pytest.mark.parametrize("fn, args, kwds", [
        (None, [], {}),
        (add, None, {}),
        (add, [], None),
        (None, None, None)
    ])
    def test_edge_cases(fn, args, kwds):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py:15: Failed
_______________________ test_edge_cases[add-args2-None] ________________________

fn = <function add at 0x7f6c35a5bb00>, args = [], kwds = None

    @pytest.mark.parametrize("fn, args, kwds", [
        (None, [], {}),
        (add, None, {}),
        (add, [], None),
        (None, None, None)
    ])
    def test_edge_cases(fn, args, kwds):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py:15: Failed
_______________________ test_edge_cases[None-None-None] ________________________

fn = None, args = None, kwds = None

    @pytest.mark.parametrize("fn, args, kwds", [
        (None, [], {}),
        (add, None, {}),
        (add, [], None),
        (None, None, None)
    ])
    def test_edge_cases(fn, args, kwds):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py::test_edge_cases[None-args0-kwds0]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py::test_edge_cases[add-None-kwds1]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py::test_edge_cases[add-args2-None]
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py::test_edge_cases[None-None-None]
============================== 4 failed in 0.11s ===============================
"""