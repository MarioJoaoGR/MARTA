
import pytest
from typing import Type, List, Dict
from flutes.structure import _no_map_type

# Define a constant for the special attribute name
_NO_MAP_INSTANCE_ATTR = '_no_map'

def test_create_subtype_from_list():
    NoMapList = _no_map_type(List)
    my_list = NoMapList([1, 2, 3])
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
________________________ test_create_subtype_from_list _________________________

    def test_create_subtype_from_list():
>       NoMapList = _no_map_type(List)

flutes/Test4DT_tests/test_flutes_structure__no_map_type_0.py:10: 
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
FAILED flutes/Test4DT_tests/test_flutes_structure__no_map_type_0.py::test_create_subtype_from_list
============================== 1 failed in 0.10s ===============================
"""