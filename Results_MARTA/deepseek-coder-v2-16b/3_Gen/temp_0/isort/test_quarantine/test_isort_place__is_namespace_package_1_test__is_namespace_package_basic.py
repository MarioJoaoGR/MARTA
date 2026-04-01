
import pytest
from pathlib import Path
from isort.place import _is_namespace_package, _is_package

@pytest.fixture(params=[Path("C:\\path\\to\\namespace_pkg"), Path("C:\\path\\to\\non_namespace_pkg")])
def namespace_pkg_path(request):
    return request.param

@pytest.fixture(params=[frozenset(['py', 'cpp']), frozenset(['txt', 'md'])])
def src_extensions(request):
    return request.param

def test_is_namespace_package_basic(namespace_pkg_path, src_extensions):
    if namespace_pkg_path == Path("C:\\path\\to\\non_namespace_pkg"):
        assert not _is_namespace_package(namespace_pkg_path, src_extensions)
    else:
        assert _is_namespace_package(namespace_pkg_path, src_extensions)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort_place__is_namespace_package_1_test__is_namespace_package_basic.py F [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
_____ test_is_namespace_package_basic[namespace_pkg_path0-src_extensions0] _____

namespace_pkg_path = PosixPath('C:\\path\\to\\namespace_pkg')
src_extensions = frozenset({'cpp', 'py'})

    def test_is_namespace_package_basic(namespace_pkg_path, src_extensions):
        if namespace_pkg_path == Path("C:\\path\\to\\non_namespace_pkg"):
            assert not _is_namespace_package(namespace_pkg_path, src_extensions)
        else:
>           assert _is_namespace_package(namespace_pkg_path, src_extensions)
E           AssertionError: assert False
E            +  where False = _is_namespace_package(PosixPath('C:\\path\\to\\namespace_pkg'), frozenset({'cpp', 'py'}))

isort/Test4DT_tests/test_isort_place__is_namespace_package_1_test__is_namespace_package_basic.py:18: AssertionError
_____ test_is_namespace_package_basic[namespace_pkg_path0-src_extensions1] _____

namespace_pkg_path = PosixPath('C:\\path\\to\\namespace_pkg')
src_extensions = frozenset({'md', 'txt'})

    def test_is_namespace_package_basic(namespace_pkg_path, src_extensions):
        if namespace_pkg_path == Path("C:\\path\\to\\non_namespace_pkg"):
            assert not _is_namespace_package(namespace_pkg_path, src_extensions)
        else:
>           assert _is_namespace_package(namespace_pkg_path, src_extensions)
E           AssertionError: assert False
E            +  where False = _is_namespace_package(PosixPath('C:\\path\\to\\namespace_pkg'), frozenset({'md', 'txt'}))

isort/Test4DT_tests/test_isort_place__is_namespace_package_1_test__is_namespace_package_basic.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_1_test__is_namespace_package_basic.py::test_is_namespace_package_basic[namespace_pkg_path0-src_extensions0]
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_1_test__is_namespace_package_basic.py::test_is_namespace_package_basic[namespace_pkg_path0-src_extensions1]
========================= 2 failed, 2 passed in 0.14s ==========================
"""