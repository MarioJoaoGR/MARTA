
import os
import pytest
from pysnooper.tracer import Tracer
from file_writer_module import FileWriter

# Ensure the test directory exists
TEST_DIR = "test_outputs"
os.makedirs(TEST_DIR, exist_ok=True)

def test_filewriter_overwrite_mode():
    file_path = os.path.join(TEST_DIR, 'test_overwrite.txt')
    writer = FileWriter(file_path, overwrite=True)
    writer.write('Hello, world!')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == 'Hello, world!'

def test_filewriter_append_mode():
    file_path = os.path.join(TEST_DIR, 'test_append.txt')
    writer = FileWriter(file_path, overwrite=True)
    writer.write('First line.')
    writer.overwrite = False
    writer.write('\nSecond line.')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == 'First line.\nSecond line.'

def test_filewriter_direct_append_mode():
    file_path = os.path.join(TEST_DIR, 'test_direct_append.txt')
    writer = FileWriter(file_path, overwrite=False)
    writer.write('Line 1.')
    writer.write('\nLine 2.')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == 'Line 1.\nLine 2.'

def test_filewriter_relative_path():
    file_path = os.path.join(TEST_DIR, 'relative_logfile.log')
    writer = FileWriter(file_path, overwrite=True)
    writer.write('Log entry.')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == 'Log entry.'

def test_filewriter_absolute_path():
    file_path = os.path.abspath(os.path.join(TEST_DIR, 'absolute_logfile.log'))
    writer = FileWriter(file_path, overwrite=True)
    writer.write('Absolute log entry.')
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    assert content == 'Absolute log entry.'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_pysnooper_tracer_FileWriter_write_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_FileWriter_write_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_FileWriter_write_0.py:5: in <module>
    from file_writer_module import FileWriter
E   ModuleNotFoundError: No module named 'file_writer_module'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_tracer_FileWriter_write_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""