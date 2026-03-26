
import pytest
from pathlib import Path
from isort.place import _is_namespace_package

@pytest.fixture
def namespace_pkg_path():
    return Path('/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/data/namespace_pkg')

def test_is_namespace_package_true(namespace_pkg_path):
    assert _is_namespace_package(namespace_pkg_path, frozenset({"py", "pyi"})) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_non_namespace_package.py F [100%]

=================================== FAILURES ===================================
________________________ test_is_namespace_package_true ________________________

namespace_pkg_path = PosixPath('/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/data/namespace_pkg')

    def test_is_namespace_package_true(namespace_pkg_path):
>       assert _is_namespace_package(namespace_pkg_path, frozenset({"py", "pyi"})) == True
E       AssertionError: assert False == True
E        +  where False = _is_namespace_package(PosixPath('/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/data/namespace_pkg'), frozenset({'py', 'pyi'}))
E        +    where frozenset({'py', 'pyi'}) = frozenset({'py', 'pyi'})

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_non_namespace_package.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_non_namespace_package.py::test_is_namespace_package_true
============================== 1 failed in 0.11s ===============================
"""