
import inspect
from collections import OrderedDict
import pytest
from pysnooper.tracer import get_local_reprs

def example_function():
    x = 10
    y = [1, 2, 3]
    frame = inspect.currentframe()
    return frame





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        frame = example_function()
        custom_repr = [(int, lambda x: f'Integer: {x}')]
>       result = get_local_reprs(frame, watch=None, custom_repr=custom_repr, max_length=None, normalize=False)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

frame = <frame at 0x7fcbd3e01d80, file '/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py', line 11, code example_function>
watch = None
custom_repr = [(<class 'int'>, <function test_happy_path.<locals>.<lambda> at 0x7fcbd3da05e0>)]
max_length = None, normalize = False

    def get_local_reprs(frame, watch=(), custom_repr=(), max_length=None, normalize=False):
        code = frame.f_code
        vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                      tuple(frame.f_locals.keys()))
    
        result_items = [(key, utils.get_shortish_repr(value, custom_repr,
                                                      max_length, normalize))
                        for key, value in frame.f_locals.items()]
        result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))
        result = collections.OrderedDict(result_items)
    
>       for variable in watch:
E       TypeError: 'NoneType' object is not iterable

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/tracer.py:36: TypeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        frame = example_function()
        result = get_local_reprs(frame, watch=[], custom_repr=[], max_length=5, normalize=True)
        expected = OrderedDict([('x', '10'), ('y', '[1, ...]')])
>       assert result == expected
E       AssertionError: assert OrderedDict([...e', '<...>')]) == OrderedDict([... '[1, ...]')])
E         
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {'y': '[...]'} != {'y': '[1, ...]'}
E         Left contains 1 more item:
E         {'frame': '<...>'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py:24: AssertionError
_____________________________ test_no_custom_repr ______________________________

    def test_no_custom_repr():
        frame = example_function()
>       result = get_local_reprs(frame, watch=None, custom_repr=[], max_length=None, normalize=False)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

frame = <frame at 0x7fcbd3e620c0, file '/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py', line 11, code example_function>
watch = None, custom_repr = [], max_length = None, normalize = False

    def get_local_reprs(frame, watch=(), custom_repr=(), max_length=None, normalize=False):
        code = frame.f_code
        vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                      tuple(frame.f_locals.keys()))
    
        result_items = [(key, utils.get_shortish_repr(value, custom_repr,
                                                      max_length, normalize))
                        for key, value in frame.f_locals.items()]
        result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))
        result = collections.OrderedDict(result_items)
    
>       for variable in watch:
E       TypeError: 'NoneType' object is not iterable

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/tracer.py:36: TypeError
________________________________ test_normalize ________________________________

    def test_normalize():
        frame = example_function()
>       result = get_local_reprs(frame, watch=None, custom_repr=[], max_length=None, normalize=True)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

frame = <frame at 0x7fcbd3e62260, file '/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py', line 11, code example_function>
watch = None, custom_repr = [], max_length = None, normalize = True

    def get_local_reprs(frame, watch=(), custom_repr=(), max_length=None, normalize=False):
        code = frame.f_code
        vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                      tuple(frame.f_locals.keys()))
    
        result_items = [(key, utils.get_shortish_repr(value, custom_repr,
                                                      max_length, normalize))
                        for key, value in frame.f_locals.items()]
        result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))
        result = collections.OrderedDict(result_items)
    
>       for variable in watch:
E       TypeError: 'NoneType' object is not iterable

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/tracer.py:36: TypeError
_______________________________ test_max_length ________________________________

    def test_max_length():
        frame = example_function()
>       result = get_local_reprs(frame, watch=None, custom_repr=[], max_length=5, normalize=False)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

frame = <frame at 0x7fcbd3e03c60, file '/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py', line 11, code example_function>
watch = None, custom_repr = [], max_length = 5, normalize = False

    def get_local_reprs(frame, watch=(), custom_repr=(), max_length=None, normalize=False):
        code = frame.f_code
        vars_order = (code.co_varnames + code.co_cellvars + code.co_freevars +
                      tuple(frame.f_locals.keys()))
    
        result_items = [(key, utils.get_shortish_repr(value, custom_repr,
                                                      max_length, normalize))
                        for key, value in frame.f_locals.items()]
        result_items.sort(key=lambda key_value: vars_order.index(key_value[0]))
        result = collections.OrderedDict(result_items)
    
>       for variable in watch:
E       TypeError: 'NoneType' object is not iterable

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/tracer.py:36: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py::test_no_custom_repr
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py::test_normalize
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_1.py::test_max_length
============================== 5 failed in 0.09s ===============================
"""