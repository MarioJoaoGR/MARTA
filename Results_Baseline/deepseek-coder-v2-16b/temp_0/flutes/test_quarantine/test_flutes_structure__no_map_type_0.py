
import pytest
from typing import Type, List, Dict
from flutes.structure import _no_map_type

def test__no_map_type_with_builtin_list():
    NoMapList = _no_map_type(List)
    my_list = NoMapList()
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

flutes/Test4DT_tests/test_flutes_structure__no_map_type_0.py F           [100%]

=================================== FAILURES ===================================
_____________________ test__no_map_type_with_builtin_list ______________________

    def test__no_map_type_with_builtin_list():
>       NoMapList = _no_map_type(List)

flutes/Test4DT_tests/test_flutes_structure__no_map_type_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

container_type = typing.List

    @lru_cache(maxsize=None)
    def _no_map_type(container_type: Type[T]) -> Type[T]:
        # Create a subtype of the container type that sets an normally inaccessible
        # special attribute on instances.
        # This is necessary because `setattr` does not work on built-in types
        # (e.g. `list`).
>       new_type = type("_no_map" + container_type.__name__,
                        (container_type,), {_NO_MAP_INSTANCE_ATTR: True})
E       TypeError: type() doesn't support MRO entry resolution; use types.new_class()

flutes/flutes/structure.py:55: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure__no_map_type_0.py::test__no_map_type_with_builtin_list
============================== 1 failed in 0.09s ===============================
"""