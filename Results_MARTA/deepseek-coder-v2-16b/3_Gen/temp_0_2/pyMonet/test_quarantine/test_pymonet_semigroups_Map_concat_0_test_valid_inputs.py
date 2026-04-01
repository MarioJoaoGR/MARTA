
import pytest
from pymonet.semigroups import Map, Semigroup

def test_valid_inputs():
    class Semigroup:
        def __init__(self, value):
            self.value = value
    
        def concat(self, other):
            if isinstance(self.value, (int, float)) and isinstance(other.value, (int, float)):
                return Semigroup(self.value + other.value)
            elif isinstance(self.value, str) and isinstance(other.value, str):
                return Semigroup(self.value + other.value)
    
    map1 = Map({'key1': Semigroup(5), 'key2': Semigroup('hello')})
    map2 = Map({'key1': Semigroup(3), 'key3': Semigroup('world')})
    
    concatenated_map = map1.concat(map2)
    
    expected_value = {'key1': Semigroup(8), 'key2': Semigroup('hello'), 'key3': Semigroup('world')}
    assert concatenated_map.value == expected_value

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

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        class Semigroup:
            def __init__(self, value):
                self.value = value
    
            def concat(self, other):
                if isinstance(self.value, (int, float)) and isinstance(other.value, (int, float)):
                    return Semigroup(self.value + other.value)
                elif isinstance(self.value, str) and isinstance(other.value, str):
                    return Semigroup(self.value + other.value)
    
        map1 = Map({'key1': Semigroup(5), 'key2': Semigroup('hello')})
        map2 = Map({'key1': Semigroup(3), 'key3': Semigroup('world')})
    
>       concatenated_map = map1.concat(map2)

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_valid_inputs.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/semigroups.py:136: in concat
    {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <dict_itemiterator object at 0x7fb586dcf010>

>       {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
    )
E   KeyError: 'key2'

pyMonet/pymonet/semigroups.py:136: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""