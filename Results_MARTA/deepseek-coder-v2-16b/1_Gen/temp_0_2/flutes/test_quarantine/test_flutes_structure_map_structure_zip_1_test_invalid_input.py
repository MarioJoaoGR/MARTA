
import pytest
from flutes.structure import map_structure_zip

def test_invalid_input():
    with pytest.raises(ValueError):
        # Try to map over two lists with different structures
        result = map_structure_zip(lambda x, y: x + y, [[1, 2], {'a': 1}])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
            # Try to map over two lists with different structures
>           result = map_structure_zip(lambda x, y: x + y, [[1, 2], {'a': 1}])

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:116: in map_structure_zip
    return [map_structure_zip(fn, xs) for xs in zip(*objs)]
flutes/flutes/structure.py:116: in <listcomp>
    return [map_structure_zip(fn, xs) for xs in zip(*objs)]
flutes/flutes/structure.py:127: in map_structure_zip
    return fn(*objs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = 1, y = 'a'

>   result = map_structure_zip(lambda x, y: x + y, [[1, 2], {'a': 1}])
E   TypeError: unsupported operand type(s) for +: 'int' and 'str'

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py:8: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.09s ===============================
"""