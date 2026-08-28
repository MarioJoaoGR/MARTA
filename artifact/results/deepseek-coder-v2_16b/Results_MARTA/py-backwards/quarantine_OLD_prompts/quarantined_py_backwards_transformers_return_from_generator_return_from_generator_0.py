
import pytest
from py_backwards.transformers.return_from_generator import return_from_generator



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def custom_generator():
            yield 1
            yield 2
            yield 3
            return_from_generator(42)
    
        gen = custom_generator()
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py:13: Failed
________________________________ test_edge_case ________________________________

    def test_edge_case():
        def custom_generator():
            yield 1
            yield 2
            yield 3
            return_from_generator(None)
    
        gen = custom_generator()
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py:24: Failed
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        def custom_generator():
            yield 1
            yield 2
            yield 3
            return_from_generator("not a number")
    
        gen = custom_generator()
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py:35: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_return_from_generator_return_from_generator_0.py::test_invalid_input
============================== 3 failed in 0.07s ===============================
"""