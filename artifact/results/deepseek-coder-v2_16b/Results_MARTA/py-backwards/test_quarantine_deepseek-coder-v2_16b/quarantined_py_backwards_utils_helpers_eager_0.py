
import pytest
from py_backwards.utils.helpers import eager


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_eager_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_eager_lambda _______________________________

    def test_eager_lambda():
        eager_function = eager(lambda: None)
>       result = eager_function()

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_eager_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = (), kwargs = {}

    @wraps(fn)
    def wrapped(*args: Any, **kwargs: Any) -> List[T]:
>       return list(fn(*args, **kwargs))
E       TypeError: 'NoneType' object is not iterable

/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/utils/helpers.py:15: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_eager_0.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_eager_0.py::test_eager_lambda
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_eager_0.py::test_invalid_input
============================== 2 failed in 0.06s ===============================
"""