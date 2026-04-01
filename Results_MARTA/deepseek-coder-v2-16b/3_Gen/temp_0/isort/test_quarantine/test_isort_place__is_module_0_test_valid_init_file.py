
import pytest
from pathlib import Path
from isort.place import _is_module

@pytest.mark.parametrize("path, expected", [
    (Path("mypackage/__init__.py"), True),
    (Path("mypackage/module.py"), True),
    (Path("notapackage/file.txt"), False)
])
def test_valid_init_file(path, expected):
    assert _is_module(path) == expected

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

isort/Test4DT_tests/test_isort_place__is_module_0_test_valid_init_file.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_valid_init_file[path0-True] _______________________

path = PosixPath('mypackage/__init__.py'), expected = True

    @pytest.mark.parametrize("path, expected", [
        (Path("mypackage/__init__.py"), True),
        (Path("mypackage/module.py"), True),
        (Path("notapackage/file.txt"), False)
    ])
    def test_valid_init_file(path, expected):
>       assert _is_module(path) == expected
E       AssertionError: assert False == True
E        +  where False = _is_module(PosixPath('mypackage/__init__.py'))

isort/Test4DT_tests/test_isort_place__is_module_0_test_valid_init_file.py:12: AssertionError
_______________________ test_valid_init_file[path1-True] _______________________

path = PosixPath('mypackage/module.py'), expected = True

    @pytest.mark.parametrize("path, expected", [
        (Path("mypackage/__init__.py"), True),
        (Path("mypackage/module.py"), True),
        (Path("notapackage/file.txt"), False)
    ])
    def test_valid_init_file(path, expected):
>       assert _is_module(path) == expected
E       AssertionError: assert False == True
E        +  where False = _is_module(PosixPath('mypackage/module.py'))

isort/Test4DT_tests/test_isort_place__is_module_0_test_valid_init_file.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_place__is_module_0_test_valid_init_file.py::test_valid_init_file[path0-True]
FAILED isort/Test4DT_tests/test_isort_place__is_module_0_test_valid_init_file.py::test_valid_init_file[path1-True]
========================= 2 failed, 1 passed in 0.11s ==========================
"""