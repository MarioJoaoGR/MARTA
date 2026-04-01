
import pytest
from flutes.structure import map_structure_zip

@pytest.mark.parametrize("objs, expected", [
    ([[1, 2], [3, 4]], [4, 6]),
    ([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], {'a': 3, 'b': 8}),
    ((('a', 'b'), ('c', 'd')), ('ac', 'bd'))
])
def test_map_structure_zip(objs, expected):
    result = map_structure_zip(lambda x, y: x + y if isinstance(x, (int, float)) else x * y, objs)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________ test_map_structure_zip[objs1-expected1] ____________________

objs = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], expected = {'a': 3, 'b': 8}

    @pytest.mark.parametrize("objs, expected", [
        ([[1, 2], [3, 4]], [4, 6]),
        ([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], {'a': 3, 'b': 8}),
        ((('a', 'b'), ('c', 'd')), ('ac', 'bd'))
    ])
    def test_map_structure_zip(objs, expected):
        result = map_structure_zip(lambda x, y: x + y if isinstance(x, (int, float)) else x * y, objs)
>       assert result == expected
E       AssertionError: assert {'a': 4, 'b': 6} == {'a': 3, 'b': 8}
E         
E         Differing items:
E         {'b': 6} != {'b': 8}
E         {'a': 4} != {'a': 3}
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py:12: AssertionError
___________________ test_map_structure_zip[objs2-expected2] ____________________

objs = (('a', 'b'), ('c', 'd')), expected = ('ac', 'bd')

    @pytest.mark.parametrize("objs, expected", [
        ([[1, 2], [3, 4]], [4, 6]),
        ([{'a': 1, 'b': 2}, {'a': 3, 'b': 4}], {'a': 3, 'b': 8}),
        ((('a', 'b'), ('c', 'd')), ('ac', 'bd'))
    ])
    def test_map_structure_zip(objs, expected):
>       result = map_structure_zip(lambda x, y: x + y if isinstance(x, (int, float)) else x * y, objs)

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:121: in map_structure_zip
    return tuple(map_structure_zip(fn, xs) for xs in zip(*objs))
flutes/flutes/structure.py:121: in <genexpr>
    return tuple(map_structure_zip(fn, xs) for xs in zip(*objs))
flutes/flutes/structure.py:127: in map_structure_zip
    return fn(*objs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 'a', y = 'c'

>   result = map_structure_zip(lambda x, y: x + y if isinstance(x, (int, float)) else x * y, objs)
E   TypeError: can't multiply sequence by non-int of type 'str'

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py::test_map_structure_zip[objs1-expected1]
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_valid_input.py::test_map_structure_zip[objs2-expected2]
========================= 2 failed, 1 passed in 0.09s ==========================
"""