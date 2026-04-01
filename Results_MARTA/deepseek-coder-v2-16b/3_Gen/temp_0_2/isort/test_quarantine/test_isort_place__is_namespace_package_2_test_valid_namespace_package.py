
import pytest
from pathlib import Path
from isort.place import _is_namespace_package, _is_package

@pytest.mark.parametrize("path, src_extensions, expected", [
    (Path("C:\\path\\to\\namespace_pkg"), frozenset({"py", "pyi"}), True),
    (Path("C:\\path\\to\\non_namespace_pkg"), frozenset({"py", "pyi"}), False),
    (Path("/Users/username/project/mynsdir"), frozenset({"py", "pyi"}), True),
])
def test_valid_namespace_package(path, src_extensions, expected):
    assert _is_namespace_package(path, src_extensions) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_valid_namespace_package.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
___________ test_valid_namespace_package[path0-src_extensions0-True] ___________

path = PosixPath('C:\\path\\to\\namespace_pkg')
src_extensions = frozenset({'py', 'pyi'}), expected = True

    @pytest.mark.parametrize("path, src_extensions, expected", [
        (Path("C:\\path\\to\\namespace_pkg"), frozenset({"py", "pyi"}), True),
        (Path("C:\\path\\to\\non_namespace_pkg"), frozenset({"py", "pyi"}), False),
        (Path("/Users/username/project/mynsdir"), frozenset({"py", "pyi"}), True),
    ])
    def test_valid_namespace_package(path, src_extensions, expected):
>       assert _is_namespace_package(path, src_extensions) == expected
E       AssertionError: assert False == True
E        +  where False = _is_namespace_package(PosixPath('C:\\path\\to\\namespace_pkg'), frozenset({'py', 'pyi'}))

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_valid_namespace_package.py:12: AssertionError
___________ test_valid_namespace_package[path2-src_extensions2-True] ___________

path = PosixPath('/Users/username/project/mynsdir')
src_extensions = frozenset({'py', 'pyi'}), expected = True

    @pytest.mark.parametrize("path, src_extensions, expected", [
        (Path("C:\\path\\to\\namespace_pkg"), frozenset({"py", "pyi"}), True),
        (Path("C:\\path\\to\\non_namespace_pkg"), frozenset({"py", "pyi"}), False),
        (Path("/Users/username/project/mynsdir"), frozenset({"py", "pyi"}), True),
    ])
    def test_valid_namespace_package(path, src_extensions, expected):
>       assert _is_namespace_package(path, src_extensions) == expected
E       AssertionError: assert False == True
E        +  where False = _is_namespace_package(PosixPath('/Users/username/project/mynsdir'), frozenset({'py', 'pyi'}))

isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_valid_namespace_package.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_valid_namespace_package.py::test_valid_namespace_package[path0-src_extensions0-True]
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_2_test_valid_namespace_package.py::test_valid_namespace_package[path2-src_extensions2-True]
========================= 2 failed, 1 passed in 0.11s ==========================
"""