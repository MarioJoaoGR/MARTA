
import pytest
from pysnooper.tracer import Tracer

def sample_function(x=10, y=2):
    my_list = [1, 2, 3]
    result = x + y * sum(my_list)
    return result







"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py F [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
___________________ test_valid_case_no_normalize_thread_info ___________________

    def test_valid_case_no_normalize_thread_info():
        tracer = Tracer(
            output='trace.log',
            watch=('x', 'y'),
            watch_explode=('my_list',),
            depth=2,
            prefix='DEBUG: ',
            overwrite=True,
            thread_info=False,
            custom_repr=((int, lambda x: f'Custom: {x}')),
            max_variable_length=100,
            normalize=False,
            relative_time=True
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:26: AssertionError
________________ test_valid_case_with_normalize_no_thread_info _________________

    def test_valid_case_with_normalize_no_thread_info():
        tracer = Tracer(
            output='trace.log',
            watch=('x', 'y'),
            watch_explode=('my_list',),
            depth=2,
            prefix='DEBUG: ',
            overwrite=True,
            thread_info=False,
            custom_repr=((int, lambda x: f'Custom: {x}')),
            max_variable_length=100,
            normalize=True,
            relative_time=True
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:44: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        tracer = Tracer(
            output=None,
            watch=[],
            watch_explode=[],
            depth=1,
            prefix='',
            overwrite=False,
            thread_info=False,
            custom_repr=(),
            max_variable_length=None,
            normalize=False,
            relative_time=False
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:62: AssertionError
----------------------------- Captured stderr call -----------------------------
Source path:... /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py
New var:....... tracer = <pysnooper.tracer.Tracer object at 0x7f876cb0ce80>
19:59:41.751699 line        61         result = sample_function()
New var:....... result = 22
19:59:41.751756 line        60     with tracer:
Elapsed time: 00:00:00.000092
_______________________________ test_custom_repr _______________________________

    def test_custom_repr():
        tracer = Tracer(
            output='trace.log',
            watch=('x', 'y'),
            watch_explode=('my_list',),
            depth=2,
            prefix='DEBUG: ',
            overwrite=True,
            thread_info=False,
            custom_repr=((int, lambda x: f'Custom: {x}')),
            max_variable_length=100,
            normalize=False,
            relative_time=True
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:80: AssertionError
___________________________ test_max_variable_length ___________________________

    def test_max_variable_length():
        tracer = Tracer(
            output='trace.log',
            watch=('x', 'y'),
            watch_explode=('my_list',),
            depth=2,
            prefix='DEBUG: ',
            overwrite=True,
            thread_info=False,
            custom_repr=((int, lambda x: f'Custom: {x}')),
            max_variable_length=5,
            normalize=False,
            relative_time=True
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:98: AssertionError
______________________________ test_relative_time ______________________________

    def test_relative_time():
        tracer = Tracer(
            output='trace.log',
            watch=('x', 'y'),
            watch_explode=('my_list',),
            depth=2,
            prefix='DEBUG: ',
            overwrite=True,
            thread_info=False,
            custom_repr=((int, lambda x: f'Custom: {x}')),
            max_variable_length=100,
            normalize=False,
            relative_time=True
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:116: AssertionError
____________________________ test_no_relative_time _____________________________

    def test_no_relative_time():
        tracer = Tracer(
            output='trace.log',
            watch=('x', 'y'),
            watch_explode=('my_list',),
            depth=2,
            prefix='DEBUG: ',
            overwrite=True,
            thread_info=False,
            custom_repr=((int, lambda x: f'Custom: {x}')),
            max_variable_length=100,
            normalize=False,
            relative_time=False
        )
        with tracer:
            result = sample_function()
>       assert result == 36
E       assert 22 == 36

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py:134: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_valid_case_no_normalize_thread_info
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_valid_case_with_normalize_no_thread_info
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_custom_repr
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_max_variable_length
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_relative_time
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_Tracer___init___0.py::test_no_relative_time
============================== 7 failed in 0.11s ===============================
"""