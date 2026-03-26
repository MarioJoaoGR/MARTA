
import pytest
from pymonet.lazy import Lazy

def square(x):
    return x * x

def double(x):
    return x * 2

@pytest.fixture
def lazy_square():
    return Lazy(square)

def test_map(lazy_square):
    mapped_lazy = lazy_square.map(double)
    assert not hasattr(mapped_lazy, 'value')
    result = mapped_lazy.fold()
    assert result == 100  # Since square of 10 is 100 and then doubled it becomes 200

def test_initialization():
    lazy = Lazy(square)
    assert lazy.constructor_fn == square
    assert not lazy.is_evaluated
    assert lazy.value is None

def test_fold(lazy_square):
    result = lazy_square.fold()
    assert result == 25  # Since square of 5 is 25

def test_map_and_fold(lazy_square):
    mapped_lazy = lazy_square.map(double)
    result = mapped_lazy.fold()
    assert result == 50  # Since square of 5 is 25 and then doubled it becomes 50

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py F.F [ 75%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________________ test_map ___________________________________

lazy_square = <pymonet.lazy.Lazy object at 0x7fcecef47a50>

    def test_map(lazy_square):
        mapped_lazy = lazy_square.map(double)
>       assert not hasattr(mapped_lazy, 'value')
E       AssertionError: assert not True
E        +  where True = hasattr(<pymonet.lazy.Lazy object at 0x7fcecdf27190>, 'value')

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py:17: AssertionError
__________________________________ test_fold ___________________________________

lazy_square = <pymonet.lazy.Lazy object at 0x7fcecdec7f90>

    def test_fold(lazy_square):
>       result = lazy_square.fold()
E       AttributeError: 'Lazy' object has no attribute 'fold'

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py:28: AttributeError
______________________________ test_map_and_fold _______________________________

lazy_square = <pymonet.lazy.Lazy object at 0x7fcecdec5250>

    def test_map_and_fold(lazy_square):
        mapped_lazy = lazy_square.map(double)
>       result = mapped_lazy.fold()
E       AttributeError: 'Lazy' object has no attribute 'fold'

pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py:33: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py::test_map
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py::test_fold
FAILED pyMonet/Test4DT_tests/test_pymonet_lazy_Lazy_map_0_test_edge_case.py::test_map_and_fold
========================= 3 failed, 1 passed in 0.09s ==========================
"""