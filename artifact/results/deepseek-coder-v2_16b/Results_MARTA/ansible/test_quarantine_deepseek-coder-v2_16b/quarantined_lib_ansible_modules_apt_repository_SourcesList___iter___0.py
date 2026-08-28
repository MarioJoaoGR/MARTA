
import pytest
from ansible.modules.apt_repository import SourcesList
import apt_pkg
import os
import glob

@pytest.fixture(scope="module")
def sourcelist():
    return SourcesList(module='test_module')

def test_sourceslist_init(sourcelist):
    assert hasattr(sourcelist, 'module')
    assert sourcelist.module == 'test_module'
    assert hasattr(sourcelist, 'files')
    assert isinstance(sourcelist.files, dict)
    assert hasattr(sourcelist, 'new_repos')
    assert isinstance(sourcelist.new_repos, set)
    assert hasattr(sourcelist, 'default_file')
    assert sourcelist.default_file is not None

def test_sourceslist_load(sourcelist):
    filespec = 'Dir::Etc::sourcelist'
    with pytest.raises(AttributeError):
        result = apt_pkg.config.find_file(filespec)
    assert sourcelist._apt_cfg_file(filespec) is not None

def test_sourceslist_iter(sourcelist):
    for file, n, enabled, source, comment in sourcelist:
        assert isinstance(file, str)
        assert isinstance(n, int)
        assert isinstance(enabled, bool)
        assert isinstance(source, str)
        if comment is not None:
            assert isinstance(comment, str)

def test_sourceslist_add_source(sourcelist):
    sourcelist.add_source('deb http://example.com/ubuntu focal main', comment='Added manually.')
    assert 'deb http://example.com/ubuntu focal main' in sourcelist.new_repos

def test_sourceslist_remove_source(sourcelist):
    sourcelist.remove_source('deb http://example.org/ubuntu bionic main')
    assert not any('deb http://example.org/ubuntu bionic main' in repo for repo in sourcelist.new_repos)

def test_sourceslist_save(sourcelist):
    sourcelist.add_source('deb http://example.com/ubuntu focal main', comment='Added manually.')
    sourcelist.save()
    assert os.path.isfile(sourcelist.default_file)

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
_ ERROR collecting test_lib_ansible_modules_apt_repository_SourcesList___iter___0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList___iter___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList___iter___0.py:4: in <module>
    import apt_pkg
E   ModuleNotFoundError: No module named 'apt_pkg'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList___iter___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.45s ===============================
"""