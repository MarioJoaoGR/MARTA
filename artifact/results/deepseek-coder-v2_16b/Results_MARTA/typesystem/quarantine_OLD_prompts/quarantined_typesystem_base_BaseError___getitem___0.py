
import pytest
from typesystem.baseclass import BaseError, Message

# Test instantiating a BaseError with a single error message
def test_BaseError_instantiation_with_single_message():
    error = BaseError(text="This field may not be blank.", code="required", key="username")
    assert isinstance(error, BaseError)
    assert len(error.messages()) == 1
    assert error.messages()[0] == "This field may not be blank."

# Test instantiating a BaseError with multiple error messages
def test_BaseError_instantiation_with_multiple_messages():
    errors = [Message(text="Invalid username.", code="invalid_key", key="username"), 
              Message(text="Username too long.", code="max_length", key="username")]
    error_with_multiple_messages = BaseError(messages=errors)
    assert isinstance(error_with_multiple_messages, BaseError)
    assert len(error_with_multiple_messages.messages()) == 2
    assert error_with_multiple_messages.messages() == ["Invalid username.", "Username too long."]

# Test accessing the error messages using __getitem__ method
def test_BaseError_accessing_messages():
    errors = [Message(text="First error", key="field1"), Message(text="Second error", key="field2")]
    error = BaseError(messages=errors)
    assert isinstance(error, BaseError)
    assert len(error.messages()) == 2
    assert error["field1"] == "First error"
    assert error["field2"] == "Second error"

# Test accessing a non-existent key in the error messages
def test_BaseError_accessing_non_existent_key():
    errors = [Message(text="First error", key="field1"), Message(text="Second error", key="field2")]
    error = BaseError(messages=errors)
    with pytest.raises(KeyError):
        error["nonexistent_key"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_typesystem_base_BaseError___getitem___0.py _______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_BaseError___getitem___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_BaseError___getitem___0.py:3: in <module>
    from typesystem.baseclass import BaseError, Message
E   ModuleNotFoundError: No module named 'typesystem.baseclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/typesystem/Test4DT_tests_deepseek-coder-v2_16b/test_typesystem_base_BaseError___getitem___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""