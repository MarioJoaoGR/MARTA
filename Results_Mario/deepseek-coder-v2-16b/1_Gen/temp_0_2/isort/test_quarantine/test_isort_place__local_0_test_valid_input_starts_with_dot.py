
from isort.place import LOCAL
from isort.config import Config

def test_valid_input_starts_with_dot():
    assert _local("module_name", Config()) is None
    assert _local(".hidden_module", Config()) == (LOCAL, "Module name started with a dot.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__local_0_test_valid_input_starts_with_dot
isort/Test4DT_tests/test_isort_place__local_0_test_valid_input_starts_with_dot.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_place__local_0_test_valid_input_starts_with_dot.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_place__local_0_test_valid_input_starts_with_dot.py:6:11: E0602: Undefined variable '_local' (undefined-variable)
isort/Test4DT_tests/test_isort_place__local_0_test_valid_input_starts_with_dot.py:7:11: E0602: Undefined variable '_local' (undefined-variable)


"""