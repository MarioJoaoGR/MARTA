
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

@pytest.mark.parametrize("processes, initializer, initargs, maxtasksperchild, context", [
    (0, None, (), None, None),
    (1, lambda: print("Initialized"), ("arg1", "arg2"), 5, {"key": "value"}),
])
def test_valid_inputs(processes, initializer, initargs, maxtasksperchild, context):
    pool = DummyPool(processes=processes, initializer=initializer, initargs=initargs, maxtasksperchild=maxtasksperchild, context=context)
    
    assert pool._process_state is not None if initializer else True
    assert pool._state == Pool()._state

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool___init___0_test_valid_inputs.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________ test_valid_inputs[1-<lambda>-initargs1-5-context1] ______________

processes = 1, initializer = <function <lambda> at 0x7fafa13b1080>
initargs = ('arg1', 'arg2'), maxtasksperchild = 5, context = {'key': 'value'}

    @pytest.mark.parametrize("processes, initializer, initargs, maxtasksperchild, context", [
        (0, None, (), None, None),
        (1, lambda: print("Initialized"), ("arg1", "arg2"), 5, {"key": "value"}),
    ])
    def test_valid_inputs(processes, initializer, initargs, maxtasksperchild, context):
>       pool = DummyPool(processes=processes, initializer=initializer, initargs=initargs, maxtasksperchild=maxtasksperchild, context=context)

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool___init___0_test_valid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:72: in __init__
    self._process_state = run_initializer().get("__state__", None)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def run_initializer():
>       initializer(*initargs)
E       TypeError: <lambda>() takes 0 positional arguments but 2 were given

flutes/flutes/multiproc.py:69: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool___init___0_test_valid_inputs.py::test_valid_inputs[1-<lambda>-initargs1-5-context1]
========================= 1 failed, 1 passed in 0.23s ==========================
"""