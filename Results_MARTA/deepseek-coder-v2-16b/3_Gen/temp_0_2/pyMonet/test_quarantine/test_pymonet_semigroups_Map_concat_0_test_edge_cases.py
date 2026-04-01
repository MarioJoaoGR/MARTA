
import pytest
from pymonet.semigroups import Map, Semigroup

def test_edge_cases():
    map1 = Map({'key1': Semigroup(5), 'key2': Semigroup('hello')})
    map2 = None
    
    with pytest.raises(TypeError):
        concatenated_map = map1.concat(map2)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        map1 = Map({'key1': Semigroup(5), 'key2': Semigroup('hello')})
        map2 = None
    
        with pytest.raises(TypeError):
>           concatenated_map = map1.concat(map2)

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_cases.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/semigroups.py:136: in concat
    {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <dict_itemiterator object at 0x7f75db6d2e80>

>       {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
    )
E   AttributeError: 'Semigroup' object has no attribute 'concat'

pyMonet/pymonet/semigroups.py:136: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""