
import pytest
from ansible.modules.apt_repository import SourcesList
import apt_pkg
import os
import glob
import tempfile

@pytest.fixture(scope="module")
def sourcelist():
    module = type('Module', (object,), {'fail_json': lambda *args: None, 'atomic_move': lambda *args: None})()
    return SourcesList(module)

# Test for saving a new source to the default file
def test_save_new_source(sourcelist):
    sourcelist.files = {}  # Reset files dictionary for each test
    sourcelist.default_file = 'Dir::Etc::sourcelist'
    sourcelist.add_source('deb http://example.com/ubuntu focal main')
    sourcelist.save()
    assert os.path.isfile(sourcelist.default_file)
    with open(sourcelist.default_file, 'r') as f:
        content = f.readlines()
    assert any('deb http://example.com/ubuntu focal main' in line for line in content)

# Test for saving an existing source to the default file
def test_save_existing_source(sourcelist):
    sourcelist.files = {}  # Reset files dictionary for each test
    sourcelist.default_file = 'Dir::Etc::sourcelist'
    sourcelist.add_source('deb http://repo2.example.org/ubuntu bionic main')
    sourcelist.save()
    assert os.path.isfile(sourcelist.default_file)
    with open(sourcelist.default_file, 'r') as f:
        content = f.readlines()
    assert any('deb http://repo2.example.org/ubuntu bionic main' in line for line in content)

# Test for saving a new source to a specific file
def test_save_new_source_to_specific_file(sourcelist):
    sourcelist.files = {}  # Reset files dictionary for each test
    sourcelist.default_file = 'Dir::Etc::sourcelist'
    sourcelist.add_source('deb http://repo3.example.org/ubuntu focal main', file='sources-focal.list')
    sourcelist.save()
    assert os.path.isfile('sources-focal.list')
    with open('sources-focal.list', 'r') as f:
        content = f.readlines()
    assert any('deb http://repo3.example.org/ubuntu focal main' in line for line in content)

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
_ ERROR collecting test_lib_ansible_modules_apt_repository_SourcesList_save_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList_save_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList_save_0.py:4: in <module>
    import apt_pkg
E   ModuleNotFoundError: No module named 'apt_pkg'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList_save_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.42s ===============================
"""