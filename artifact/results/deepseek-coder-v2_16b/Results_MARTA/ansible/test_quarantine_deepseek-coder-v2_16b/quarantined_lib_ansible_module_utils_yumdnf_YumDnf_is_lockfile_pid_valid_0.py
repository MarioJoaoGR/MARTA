
import pytest
from ansible.module_utils.yumdnf import YumDnf


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_yumdnf_YumDnf_is_lockfile_pid_valid_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        module = {
            'allow_downgrade': True,
            'autoremove': False,
            'bugfix': True,
            'cacheonly': False,
            'conf_file': '/etc/yum.conf',
            'disable_excludes': 'all',
            'disable_gpg_check': True,
            'disable_plugin': False,
            'disablerepo': ['updates'],
            'download_only': False,
            'download_dir': '/var/cache/yum',
            'enable_plugin': True,
            'enablerepo': ['epel'],
            'exclude': ['kernel*'],
            'installroot': '/opt',
            'install_repoquery': True,
            'install_weak_deps': True,
            'list': True,
            'names': ['vim', 'git'],
            'releasever': '7',
            'security': False,
            'skip_broken': False,
            'state': 'present',
            'update_only': False,
            'update_cache': True,
            'validate_certs': True,
            'lock_timeout': 60
        }
    
>       yum_dnf = YumDnf(module=module)
E       TypeError: Can't instantiate abstract class YumDnf with abstract methods is_lockfile_pid_valid, run

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_yumdnf_YumDnf_is_lockfile_pid_valid_0.py:36: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        module = {
            'allow_downgrade': True,
            'autoremove': False,
            'bugfix': True,
            'cacheonly': False,
            'conf_file': '/etc/yum.conf',
            'disable_excludes': 'all',
            'disable_gpg_check': True,
            'disable_plugin': False,
            'disablerepo': ['updates'],
            'download_only': False,
            'download_dir': '/var/cache/yum',
            'enable_plugin': True,
            'enablerepo': ['epel'],
            'exclude': ['kernel*'],
            'installroot': '/opt',
            'install_repoquery': True,
            'install_weak_deps': True,
            'list': True,
            'names': ['vim git'],  # Contains a space
            'releasever': '7',
            'security': False,
            'skip_broken': False,
            'state': 'present',
            'update_only': False,
            'update_cache': True,
            'validate_certs': True,
            'lock_timeout': 60
        }
    
        with pytest.raises(Exception) as e:
            YumDnf(module=module)
    
>       assert str(e.value) == "It appears that a space separated string of packages was passed in as an argument. To operate on several packages, pass a comma separated string of packages or a list of packages.", f"Expected specific error message: {str(e.value)}"
E       AssertionError: Expected specific error message: Can't instantiate abstract class YumDnf with abstract methods is_lockfile_pid_valid, run
E       assert "Can't instan...id_valid, run" == 'It appears t... of packages.'
E         
E         - It appears that a space separated string of packages was passed in as an argument. To operate on several packages, pass a comma separated string of packages or a list of packages.
E         + Can't instantiate abstract class YumDnf with abstract methods is_lockfile_pid_valid, run

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_yumdnf_YumDnf_is_lockfile_pid_valid_0.py:73: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_yumdnf_YumDnf_is_lockfile_pid_valid_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_yumdnf_YumDnf_is_lockfile_pid_valid_0.py::test_invalid_input
============================== 2 failed in 0.32s ===============================
"""