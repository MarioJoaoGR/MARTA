
from pathlib import Path
import pytest
from isort.place import _is_namespace_package

@pytest.fixture
def valid_namespace_pkg(tmp_path):
    pkg_dir = tmp_path / "mynsdir"
    pkg_dir.mkdir()
    (pkg_dir / "__init__.py").touch()
    return pkg_dir

@pytest.fixture
def invalid_namespace_pkg(tmp_path):
    pkg_dir = tmp_path / "mynsdir"
    pkg_dir.mkdir()
    return pkg_dir

def test_valid_namespace_package(valid_namespace_pkg):
    assert _is_namespace_package(valid_namespace_pkg, frozenset({"py", "pyi"})) == True

def test_invalid_namespace_package(invalid_namespace_pkg):
    assert _is_namespace_package(invalid_namespace_pkg, frozenset({"py", "pyi"})) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_namespace_package _________________________

valid_namespace_pkg = PosixPath('/tmp/pytest-of-joaovitorino/pytest-15/test_valid_namespace_package0/mynsdir')

    def test_valid_namespace_package(valid_namespace_pkg):
>       assert _is_namespace_package(valid_namespace_pkg, frozenset({"py", "pyi"})) == True
E       AssertionError: assert False == True
E        +  where False = _is_namespace_package(PosixPath('/tmp/pytest-of-joaovitorino/pytest-15/test_valid_namespace_package0/mynsdir'), frozenset({'py', 'pyi'}))
E        +    where frozenset({'py', 'pyi'}) = frozenset({'py', 'pyi'})

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_invalid_input.py:20: AssertionError
________________________ test_invalid_namespace_package ________________________

invalid_namespace_pkg = PosixPath('/tmp/pytest-of-joaovitorino/pytest-15/test_invalid_namespace_package0/mynsdir')

    def test_invalid_namespace_package(invalid_namespace_pkg):
>       assert _is_namespace_package(invalid_namespace_pkg, frozenset({"py", "pyi"})) == False
E       AssertionError: assert True == False
E        +  where True = _is_namespace_package(PosixPath('/tmp/pytest-of-joaovitorino/pytest-15/test_invalid_namespace_package0/mynsdir'), frozenset({'py', 'pyi'}))
E        +    where frozenset({'py', 'pyi'}) = frozenset({'py', 'pyi'})

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_invalid_input.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_invalid_input.py::test_valid_namespace_package
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_invalid_input.py::test_invalid_namespace_package
============================== 2 failed in 0.14s ===============================
"""