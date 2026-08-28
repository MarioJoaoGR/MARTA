
import pytest
from ansible.module_utils.facts.packages import get_all_subclasses, PkgMgr
from unittest.mock import patch

def get_all_pkg_managers():
    """
    Retrieves a dictionary of all package managers.

    This function scans through the subclasses of `PkgMgr` and filters out instances of `CLIMgr` and `LibMgr`. It then returns a dictionary where the keys are the lowercase names of the remaining package manager classes, and the values are the class objects themselves.

    Returns:
        dict: A dictionary mapping the lowercase names of package managers to their respective class objects.

    Examples:
        >>> get_all_pkg_managers()
        {'dpkg': <class 'PkgMgr'>, 'apt': <class 'AptMgr'>, ...}

    Note:
        - The function assumes that `get_all_subclasses` and `PkgMgr`, along with its subclasses (`CLIMgr`, `LibMgr`, etc.), are defined elsewhere in the codebase.
        - This function is useful for programmatically accessing all available package managers, which can be particularly helpful when automating system administration tasks or software installations that require specific package managers.
    """
    return dict([(obj.__name__.lower(), obj) for obj in get_all_subclasses(PkgMgr) if obj not in (CLIMgr, LibMgr)])


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        class CLIMgr(PkgMgr): pass
        class LibMgr(PkgMgr): pass
        class AptMgr(PkgMgr): pass
    
        with patch('ansible.module_utils.facts.packages.get_all_subclasses', return_value=[PkgMgr, CLIMgr, LibMgr, AptMgr]):
>           pkg_managers = get_all_pkg_managers()

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py:31: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py:23: in get_all_pkg_managers
    return dict([(obj.__name__.lower(), obj) for obj in get_all_subclasses(PkgMgr) if obj not in (CLIMgr, LibMgr)])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <set_iterator object at 0x7f1cea776080>

>   return dict([(obj.__name__.lower(), obj) for obj in get_all_subclasses(PkgMgr) if obj not in (CLIMgr, LibMgr)])
E   NameError: name 'CLIMgr' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py:23: NameError
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        class InvalidPkgMgr(object): pass
        with patch('ansible.module_utils.facts.packages.get_all_subclasses', return_value=[InvalidPkgMgr]):
            with pytest.raises(TypeError):
>               get_all_pkg_managers()

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py:41: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py:23: in get_all_pkg_managers
    return dict([(obj.__name__.lower(), obj) for obj in get_all_subclasses(PkgMgr) if obj not in (CLIMgr, LibMgr)])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <set_iterator object at 0x7f1cea243800>

>   return dict([(obj.__name__.lower(), obj) for obj in get_all_subclasses(PkgMgr) if obj not in (CLIMgr, LibMgr)])
E   NameError: name 'CLIMgr' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py:23: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_get_all_pkg_managers_0.py::test_error_handling
============================== 2 failed in 0.37s ===============================
"""