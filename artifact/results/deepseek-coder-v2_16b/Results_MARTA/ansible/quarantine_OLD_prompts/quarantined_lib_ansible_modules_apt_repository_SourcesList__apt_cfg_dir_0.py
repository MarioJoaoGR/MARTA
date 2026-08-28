
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.apt_repository import SourcesList

@pytest.fixture(autouse=True)
def mock_apt_pkg():
    with patch('ansible.modules.apt_repository.apt_pkg'):
        apt_pkg.config = MagicMock()
        yield

class TestSourcesList:
    
    @patch('os.path.isfile', return_value=True)
    def test_sourceslist_init(self, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        assert sourcelist.default_file == '/etc/apt/sources.list'
    
    @patch('os.path.isfile', return_value=True)
    def test_sourceslist_load(self, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        assert 'Dir::Etc::sourcelist' in sourcelist.files
    
    @patch('ansible.modules.apt_repository._apt_cfg_dir', return_value='/etc/apt')
    def test_sourceslist_default_file(self, mock_cfg_dir):
        sourcelist = SourcesList(module='my_module')
        assert sourcelist.default_file == '/etc/apt/sources.list'
    
    @patch('ansible.modules.apt_repository._apt_cfg_dir', return_value='/etc/apt')
    def test_sourceslist_apt_cfg_dir(self, mock_cfg_dir):
        sourcelist = SourcesList(module='my_module')
        assert sourcelist._apt_cfg_dir('Dir::Etc::sourceparts') == '/etc/apt'
    
    @patch('os.path.isfile', return_value=True)
    def test_sourceslist_parse(self, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        valid, enabled, source, comment = sourcelist._parse('deb http://example.com/ubuntu focal main')
        assert valid and enabled
    
    @patch('os.path.isfile', return_value=True)
    def test_sourceslist_add_source(self, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        sourcelist.add_source('deb http://example.com/ubuntu focal main', comment='Added by my script')
        assert 'deb http://example.com/ubuntu focal main' in sourcelist.files['/etc/apt/sources.list']
    
    @patch('os.path.isfile', return_value=True)
    def test_sourceslist_remove_source(self, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        sourcelist.remove_source('deb http://example.org/ubuntu bionic main')
        assert 'deb http://example.org/ubuntu bionic main' not in sourcelist.files['/etc/apt/sources.list']
    
    @patch('os.path.isfile', return_value=True)
    def test_sourceslist_save(self, mock_isfile):
        sourcelist = SourcesList(module='my_module')
        sourcelist.save()
        assert sourcelist.files['/etc/apt/sources.list'] == ['deb http://example.com/ubuntu focal main', 'deb http://example.org/ubuntu bionic main']
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 8 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py E [ 12%]
EEEEEEE                                                                  [100%]

==================================== ERRORS ====================================
___________ ERROR at setup of TestSourcesList.test_sourceslist_init ____________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
___________ ERROR at setup of TestSourcesList.test_sourceslist_load ____________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
_______ ERROR at setup of TestSourcesList.test_sourceslist_default_file ________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
________ ERROR at setup of TestSourcesList.test_sourceslist_apt_cfg_dir ________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
___________ ERROR at setup of TestSourcesList.test_sourceslist_parse ___________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
________ ERROR at setup of TestSourcesList.test_sourceslist_add_source _________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
_______ ERROR at setup of TestSourcesList.test_sourceslist_remove_source _______

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
___________ ERROR at setup of TestSourcesList.test_sourceslist_save ____________

    @pytest.fixture(autouse=True)
    def mock_apt_pkg():
        with patch('ansible.modules.apt_repository.apt_pkg'):
>           apt_pkg.config = MagicMock()
E           NameError: name 'apt_pkg' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py:9: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_init
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_load
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_default_file
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_apt_cfg_dir
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_parse
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_add_source
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_remove_source
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_apt_repository_SourcesList__apt_cfg_dir_0.py::TestSourcesList::test_sourceslist_save
============================== 8 errors in 0.39s ===============================
"""