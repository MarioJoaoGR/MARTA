
import pytest
from ansible.utils.version import LooseVersion
from SemanticVersion import SemanticVersion, from_loose_version

def test_from_loose_version_valid():
    loose_version = LooseVersion('1.2.3')
    semantic_version = from_loose_version(loose_version)
    assert semantic_version.major == 1
    assert semantic_version.minor == 2
    assert semantic_version.patch == 3
    assert semantic_version.prerelease == ()
    assert semantic_version.buildmetadata == ()

def test_from_loose_version_invalid():
    loose_version = LooseVersion('1.2')  # Missing patch version
    with pytest.raises(ValueError):
        from_loose_version(loose_version)

def test_from_loose_version_non_integer():
    loose_version = LooseVersion('1.2.3a')  # Contains non-integer character
    with pytest.raises(ValueError):
        from_loose_version(loose_version)

def test_from_loose_version_extra():
    loose_version = LooseVersion('1.2.3+build123')
    semantic_version = from_loose_version(loose_version)
    assert semantic_version.major == 1
    assert semantic_version.minor == 2
    assert semantic_version.patch == 3
    assert semantic_version.prerelease == ()
    assert semantic_version.buildmetadata == ('build', '123')

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
_ ERROR collecting test_lib_ansible_utils_version_SemanticVersion_from_loose_version_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion_from_loose_version_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion_from_loose_version_0.py:4: in <module>
    from SemanticVersion import SemanticVersion, from_loose_version
E   ModuleNotFoundError: No module named 'SemanticVersion'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion_from_loose_version_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.43s ===============================
"""