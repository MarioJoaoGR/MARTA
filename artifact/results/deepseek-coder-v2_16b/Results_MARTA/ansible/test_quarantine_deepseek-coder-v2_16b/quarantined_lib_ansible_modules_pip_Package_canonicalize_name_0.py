
import pytest
from ansible.modules.pip import Package
import re



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_package_name ___________________________

    def test_invalid_package_name():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py:7: Failed
__________________________ test_has_version_specifier __________________________

    def test_has_version_specifier():
        pkg = Package("requests", "2.25.1")
>       assert pkg.has_version_specifier() is True
E       TypeError: 'bool' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py:12: TypeError
__________________________ test_no_version_specifier ___________________________

    def test_no_version_specifier():
        pkg = Package("setuptools")
>       assert pkg.has_version_specifier() is False
E       TypeError: 'bool' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py:16: TypeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/modules/pip.py:280
  /opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/modules/pip.py:280: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import Requirement

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py::test_invalid_package_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py::test_has_version_specifier
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_pip_Package_canonicalize_name_0.py::test_no_version_specifier
========================= 3 failed, 1 warning in 0.41s =========================
"""