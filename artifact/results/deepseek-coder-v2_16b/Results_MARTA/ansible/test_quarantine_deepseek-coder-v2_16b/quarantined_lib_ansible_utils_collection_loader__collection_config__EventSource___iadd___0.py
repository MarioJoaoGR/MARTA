
import pytest
from your_module import _EventSource

# Test adding a handler
def test_add_handler():
    event_source = _EventSource()
    
    def handle1():
        pass
    
    event_source.add_handler(handle1)
    assert handle1 in event_source._handlers

# Test removing a handler
def test_remove_handler():
    event_source = _EventSource()
    
    def handle1():
        pass
    
    event_source.add_handler(handle1)
    event_source.remove_handler(handle1)
    assert handle1 not in event_source._handlers

# Test triggering an event with multiple handlers
def test_trigger_event():
    event_source = _EventSource()
    
    called_handlers = []
    
    def handle1():
        called_handlers.append(handle1)
    
    def handle2():
        called_handlers.append(handle2)
    
    event_source.add_handler(handle1)
    event_source.add_handler(handle2)
    event_source.trigger_event()
    
    assert len(called_handlers) == 2
    assert handle1 in called_handlers
    assert handle2 in called_handlers

# Test adding a non-callable handler raises ValueError
def test_add_non_callable_handler():
    event_source = _EventSource()
    
    with pytest.raises(ValueError):
        event_source.add_handler(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_utils_collection_loader__collection_config__EventSource___iadd___0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__EventSource___iadd___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__EventSource___iadd___0.py:3: in <module>
    from your_module import _EventSource
E   ModuleNotFoundError: No module named 'your_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_config__EventSource___iadd___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.37s ===============================
"""