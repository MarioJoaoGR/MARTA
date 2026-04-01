
import pytest
from flutes.structure import map_structure_zip

def test_edge_case():
    with pytest.raises(ValueError):
        map_structure_zip(lambda a, b: a + b, [[1, 2], [3, 4], {5, 6}])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with pytest.raises(ValueError):
>           map_structure_zip(lambda a, b: a + b, [[1, 2], [3, 4], {5, 6}])

flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_edge_case.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/structure.py:116: in map_structure_zip
    return [map_structure_zip(fn, xs) for xs in zip(*objs)]
flutes/flutes/structure.py:116: in <listcomp>
    return [map_structure_zip(fn, xs) for xs in zip(*objs)]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fn = <function test_edge_case.<locals>.<lambda> at 0x7fb9ebbb09a0>
objs = (1, 3, 5)

    @no_type_check
    def map_structure_zip(fn: Callable[..., R], objs: Sequence[Collection[T]]) -> Collection[R]:
        r"""Map a function over tuples formed by taking one elements from each (possibly nested) collection. Each collection
        must have identical structures.
    
        .. note::
            Although identical structures are required, it is not enforced by assertions. The structure of the first
            collection is assumed to be the structure for all collections.
    
        :param fn: The function to call on elements.
        :param objs: The list of collections to map function over.
        :return: A collection with the same structure, with elements mapped.
        """
        obj = objs[0]
        if obj.__class__ in _NO_MAP_TYPES or hasattr(obj, _NO_MAP_INSTANCE_ATTR):
            return fn(*objs)
        if isinstance(obj, list):
            return [map_structure_zip(fn, xs) for xs in zip(*objs)]
        if isinstance(obj, tuple):
            if hasattr(obj, '_fields'):  # namedtuple
                return type(obj)(*[map_structure_zip(fn, xs) for xs in zip(*objs)])
            else:
                return tuple(map_structure_zip(fn, xs) for xs in zip(*objs))
        if isinstance(obj, dict):
            # could be `OrderedDict`
            return type(obj)((k, map_structure_zip(fn, [o[k] for o in objs])) for k in obj.keys())
        if isinstance(obj, set):
            raise ValueError("Structures cannot contain `set` because it's unordered")
>       return fn(*objs)
E       TypeError: test_edge_case.<locals>.<lambda>() takes 2 positional arguments but 3 were given

flutes/flutes/structure.py:127: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_zip_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.10s ===============================
"""