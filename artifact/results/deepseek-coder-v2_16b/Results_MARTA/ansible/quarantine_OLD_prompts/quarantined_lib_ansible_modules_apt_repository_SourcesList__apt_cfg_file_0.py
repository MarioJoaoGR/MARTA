
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.apt_repository import SourcesList
import apt_pkg
import os
import glob

@pytest.fixture(autouse=True)
def mock_apt_config():
    with patch('ansible.modules.apt_repository.apt_pkg.config'):
        yield

class TestSourcesList:
    
    @patch('ansible.modules.apt_repository.os.path.isfile', return_value=True)
    @patch('ansible.modules.apt_repository.glob.iglob', return_value=['/mocked/dir1', '/mocked/dir2'])
    def test_sourceslist_init(self, mock_glob, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        assert sourcelist.default_file == sourcelist._apt_cfg_file('Dir::Etc::sourcelist')
    
    @patch('ansible.modules.apt_repository.os.path.isfile', return_value=True)
    @patch('ansible.modules.apt_repository.glob.iglob', return_value=[])
    def test_sourceslist_load(self, mock_glob, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        assert sourcelist.default_file == sourcelist._apt_cfg_file('Dir::Etc::sourcelist')
    
    @patch('ansible.modules.apt_repository.apt_pkg.config.find_file', side_effect=AttributeError)
    def test_sourceslist__apt_cfg_file(self, mock_find_file):
        with pytest.raises(AttributeError):
            sourcelist = SourcesList(module='my_module')

if __name__ == '__main__':
    pytest.main()

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
_ ERROR collecting test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_file_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_file_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_file_0.py:5: in <module>
    import apt_pkg
E   ModuleNotFoundError: No module named 'apt_pkg'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_file_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.43s ===============================
"""