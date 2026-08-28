
import pytest
from distutils.version import StrictVersion
from flutils.packagesclass._versionpart import _VersionPart
from typing import Tuple, Union, Dict, Any, Generator, cast

# Assuming _each_version_part is defined in the same module or can be imported correctly
def test_each_version_part_with_prerelease():
    ver = StrictVersion('1.2.3rc4')
    parts = list(_each_version_part(ver))
    assert len(parts) == 3, "Expected three version parts"
    assert parts[0].pos == 0 and parts[0].txt == '1' and parts[0].num == 1 and parts[0].name == 'major', "First part should be major with value 1"
    assert parts[1].pos == 1 and parts[1].txt == '2' and parts[1].num == 2 and parts[1].name == 'minor', "Second part should be minor with value 2"
    assert parts[2].pos == 2 and parts[2].txt == '' and parts[2].num == 0 and parts[2].pre_txt == 'rc' and parts[2].pre_num == 4, "Third part should include prerelease info with rc and number 4"

def test_each_version_part_without_prerelease():
    ver = StrictVersion('1.2.3')
    parts = list(_each_version_part(ver))
    assert len(parts) == 3, "Expected three version parts"
    assert parts[0].pos == 0 and parts[0].txt == '1' and parts[0].num == 1 and parts[0].name == 'major', "First part should be major with value 1"
    assert parts[1].pos == 1 and parts[1].txt == '2' and parts[1].num == 2 and parts[1].name == 'minor', "Second part should be minor with value 2"
    assert parts[2].pos == 2 and parts[2].txt == '3' and parts[2].num == 3 and parts[2].pre_txt == '' and parts[2].pre_num == -1, "Third part should not include prerelease info as it is the final version"

def test_each_version_part_custom_version():
    class MyCustomVersion:
        def __init__(self, version, prerelease=None):
            self.version = version
            self.prerelease = prerelease

    ver = MyCustomVersion(version=(1, 2, 3), prerelease=('rc', 4))
    parts = list(_each_version_part(ver))
    assert len(parts) == 3, "Expected three version parts"
    assert parts[0].pos == 0 and parts[0].txt == '1' and parts[0].num == 1 and parts[0].name == 'major', "First part should be major with value 1"
    assert parts[1].pos == 1 and parts[1].txt == '2' and parts[1].num == 2 and parts[1].name == 'minor', "Second part should be minor with value 2"
    assert parts[2].pos == 2 and parts[2].txt == '' and parts[2].num == 0 and parts[2].pre_txt == 'rc' and parts[2].pre_num == 4, "Third part should include prerelease info with rc and number 4"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________ ERROR collecting test_flutils_packages__each_version_part_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__each_version_part_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__each_version_part_0.py:4: in <module>
    from flutils.packagesclass._versionpart import _VersionPart
E   ModuleNotFoundError: No module named 'flutils.packagesclass'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__each_version_part_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""