
import pytest
from flutes.structure import map_structure_zip
from collections.abc import Callable, Collection, Sequence

def test_invalid_inputs():
    with pytest.raises(ValueError):
        # Test case for invalid inputs where structures contain `set` which is unordered
        map_structure_zip(lambda x: x, [{'a': 1}, {'b': 2}])

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

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
            # Test case for invalid inputs where structures contain `set` which is unordered
>           map_structure_zip(lambda x: x, [{'a': 1}, {'b': 2}])

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_invalid_inputs.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:124: in map_structure_zip
    return type(obj)((k, map_structure_zip(fn, [o[k] for o in objs])) for k in obj.keys())
flutes/flutes/structure.py:124: in <genexpr>
    return type(obj)((k, map_structure_zip(fn, [o[k] for o in objs])) for k in obj.keys())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7fc304141d50>

>   return type(obj)((k, map_structure_zip(fn, [o[k] for o in objs])) for k in obj.keys())
E   KeyError: 'a'

flutes/flutes/structure.py:124: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.11s ===============================
"""