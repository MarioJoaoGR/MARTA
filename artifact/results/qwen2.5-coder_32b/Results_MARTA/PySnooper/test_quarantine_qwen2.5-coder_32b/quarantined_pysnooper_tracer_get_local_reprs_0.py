
import inspect
from collections import OrderedDict
import pytest
from pysnooper.tracer import get_local_reprs

def example_function():
    x = 10
    y = [1, 2, 3]
    frame = inspect.currentframe()
    return get_local_reprs(frame)

def example_function_with_edge_cases():
    x = None
    y = []
    frame = inspect.currentframe()
    return get_local_reprs(frame)

def custom_repr_int(x):
    return f"Integer: {x}"

def example_function_with_custom_repr():
    x = 10
    y = [1, 2, 3]
    conditions = [(int, custom_repr_int)]
    frame = inspect.currentframe()
    return get_local_reprs(frame, custom_repr=conditions)

def example_function_with_max_length():
    x = "This is a very long string that should be truncated."
    frame = inspect.currentframe()
    return get_local_reprs(frame, max_length=10)

def example_function_with_normalize():
    x = [1, 2, 3]
    y = {'key': 'value'}
    frame = inspect.currentframe()
    return get_local_reprs(frame, normalize=True)





"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        result = example_function()
        expected = OrderedDict([('x', '10'), ('y', '[1, 2, 3]')])
>       assert result == expected
E       assert OrderedDict([..._function>")]) == OrderedDict([...'[1, 2, 3]')])
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 1 more item:
E         {'frame': '<frame at 0x7f1d7ecf1d80, file '
E                   "'/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py', "
E                   'line 11, code example_function>'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py:43: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        result = example_function_with_edge_cases()
        expected = OrderedDict([('x', 'None'), ('y', '[]')])
>       assert result == expected
E       assert OrderedDict([...dge_cases>")]) == OrderedDict([... ('y', '[]')])
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 1 more item:
E         {'frame': '<frame at 0x7f1d7ed0d700, file '
E                   "'/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py', "
E                   'line 17, code example_function_with_edge_cases>'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py:48: AssertionError
_______________________________ test_custom_repr _______________________________

    def test_custom_repr():
        result = example_function_with_custom_repr()
        expected = OrderedDict([('x', 'Integer: 10'), ('y', '[1, 2, 3]')])
>       assert result == expected
E       assert OrderedDict([...stom_repr>")]) == OrderedDict([...'[1, 2, 3]')])
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 2 more items:
E         {'conditions': "[(<class 'int'>, <function custom_repr_int at "
E                        '0x7f1d7ec8add0>)]',
E          'frame': '<frame at 0x7f1d7ed3cac0, file '
E                   "'/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py', "
E                   'line 27, code example_function_with_custom_repr>'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py:53: AssertionError
_______________________________ test_max_length ________________________________

    def test_max_length():
        result = example_function_with_max_length()
        expected = OrderedDict([('x', "This is ...")])
>       assert result['x'] == expected['x']
E       assert "'Th...ed.'" == 'This is ...'
E         
E         - This is ...
E         + 'Th...ed.'

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py:58: AssertionError
________________________________ test_normalize ________________________________

    def test_normalize():
        result = example_function_with_normalize()
        expected = OrderedDict([('x', '[1, 2, 3]'), ('y', "{'key': 'value'}")])
>       assert result == expected
E       assert OrderedDict([...normalize>")]) == OrderedDict([...: 'value'}")])
E         
E         Omitting 2 identical items, use -vv to show
E         Left contains 1 more item:
E         {'frame': '<frame, file '
E                   "'/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py', "
E                   'line 38, code example_function_with_normalize>'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py:63: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py::test_custom_repr
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py::test_max_length
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_get_local_reprs_0.py::test_normalize
============================== 5 failed in 0.06s ===============================
"""