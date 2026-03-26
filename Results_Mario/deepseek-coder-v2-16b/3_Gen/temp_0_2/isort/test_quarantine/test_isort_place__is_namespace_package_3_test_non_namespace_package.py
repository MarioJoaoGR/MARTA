
import pytest
from pathlib import Path
from isort.place import _is_namespace_package, _is_package

@pytest.fixture(params=[True, False])
def namespace_pkg_path(request):
    if request.param:
        temp_dir = Path("/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_true0/mynsdir")
        temp_dir.mkdir(parents=True, exist_ok=True)
        (temp_dir / "__init__.py").touch()
        return temp_dir
    else:
        with pytest.raises(FileNotFoundError):
            Path("/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_fals0/nonnsdir").mkdir()

def test_is_namespace_package_true(namespace_pkg_path):
    assert _is_namespace_package(namespace_pkg_path, frozenset({"py", "pyi"})) == True

def test_is_namespace_package_false():
    non_namespace_pkg_path = Path("/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_fals0/nonnsdir")
    with pytest.raises(FileNotFoundError):
        non_namespace_pkg_path.mkdir()

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

isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py F [ 33%]
EF                                                                       [100%]

==================================== ERRORS ====================================
___________ ERROR at setup of test_is_namespace_package_true[False] ____________

request = <SubRequest 'namespace_pkg_path' for <Function test_is_namespace_package_true[False]>>

    @pytest.fixture(params=[True, False])
    def namespace_pkg_path(request):
        if request.param:
            temp_dir = Path("/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_true0/mynsdir")
            temp_dir.mkdir(parents=True, exist_ok=True)
            (temp_dir / "__init__.py").touch()
            return temp_dir
        else:
>           with pytest.raises(FileNotFoundError):
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py:14: Failed
=================================== FAILURES ===================================
_____________________ test_is_namespace_package_true[True] _____________________

namespace_pkg_path = PosixPath('/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_true0/mynsdir')

    def test_is_namespace_package_true(namespace_pkg_path):
>       assert _is_namespace_package(namespace_pkg_path, frozenset({"py", "pyi"})) == True
E       AssertionError: assert False == True
E        +  where False = _is_namespace_package(PosixPath('/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_true0/mynsdir'), frozenset({'py', 'pyi'}))
E        +    where frozenset({'py', 'pyi'}) = frozenset({'py', 'pyi'})

isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py:18: AssertionError
_______________________ test_is_namespace_package_false ________________________

    def test_is_namespace_package_false():
        non_namespace_pkg_path = Path("/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_fals0/nonnsdir")
        with pytest.raises(FileNotFoundError):
>           non_namespace_pkg_path.mkdir()

isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = PosixPath('/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_fals0/nonnsdir')
mode = 511, parents = False, exist_ok = False

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        """
        Create a new directory at this given path.
        """
        try:
>           os.mkdir(self, mode)
E           FileExistsError: [Errno 17] File exists: '/tmp/pytest-of-joaovitorino/pytest-46/test_is_namespace_package_fals0/nonnsdir'

/usr/local/lib/python3.11/pathlib.py:1116: FileExistsError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py::test_is_namespace_package_true[True]
FAILED isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py::test_is_namespace_package_false
ERROR isort/Test4DT_tests/test_isort_place__is_namespace_package_3_test_non_namespace_package.py::test_is_namespace_package_true[False]
========================== 2 failed, 1 error in 0.15s ==========================
"""