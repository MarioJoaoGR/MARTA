
import pytest
from ansible.module_utils.connection import Connection
import os
import hashlib
import cPickle as pickle

def write_to_file_descriptor(fd, obj):
    """Handles making sure all data is properly written to file descriptor fd."""
    src = pickle.dumps(obj, protocol=0)
    src = src.replace(b'\r', br'\r')
    data_hash = hashlib.sha1(src).hexdigest().encode()

    os.write(fd, b'%d\n' % len(src))
    os.write(fd, src)
    os.write(fd, b'%s\n' % data_hash)

@pytest.fixture
def setup_connection():
    return Connection()

def test_write_to_file_descriptor_simple_object(setup_connection):
    fd = setup_connection.open_channel()
    obj = {'key': 'value'}
    write_to_file_descriptor(fd, obj)
    
    # Read the written data from the file descriptor
    os.write(fd, b'read\n')  # Simulate reading command
    length_line = os.read(fd, 1024).decode().strip()
    assert int(length_line) == len(pickle.dumps(obj))
    
    data = os.read(fd, int(length_line)).decode()
    assert pickle.loads(data.replace(r'\r', b'\r')) == obj
    
    hash_line = os.read(fd, 40).decode().strip()
    assert hashlib.sha1(pickle.dumps(obj)).hexdigest() == hash_line

def test_write_to_file_descriptor_large_object(setup_connection):
    fd = setup_connection.open_channel()
    large_obj = [x for x in range(10000)]
    write_to_file_descriptor(fd, large_obj)
    
    # Read the written data from the file descriptor
    os.write(fd, b'read\n')  # Simulate reading command
    length_line = os.read(fd, 1024).decode().strip()
    assert int(length_line) == len(pickle.dumps(large_obj))
    
    data = os.read(fd, int(length_line)).decode()
    assert pickle.loads(data.replace(r'\r', b'\r')) == large_obj
    
    hash_line = os.read(fd, 40).decode().strip()
    assert hashlib.sha1(pickle.dumps(large_obj)).hexdigest() == hash_line

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
_ ERROR collecting test_lib_ansible_module_utils_connection_write_to_file_descriptor_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_write_to_file_descriptor_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_write_to_file_descriptor_0.py:6: in <module>
    import cPickle as pickle
E   ModuleNotFoundError: No module named 'cPickle'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_connection_write_to_file_descriptor_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.38s ===============================
"""