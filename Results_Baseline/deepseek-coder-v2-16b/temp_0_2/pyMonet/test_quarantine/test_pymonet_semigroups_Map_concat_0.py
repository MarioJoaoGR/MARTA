
# Module: pymonet.semigroups
import pytest
from pymonet.semigroups import Map, Semigroup

# Test initialization of Map with a dictionary of Semigroup instances
def test_map_initialization():
    m1 = Map({'a': Semigroup(1), 'b': Semigroup(2)})
    assert m1.value == {'a': Semigroup(1), 'b': Semigroup(2)}

# Test concatenation of two maps with the same keys
def test_concat_same_keys():
    m1 = Map({'a': Semigroup(1), 'b': Semigroup(2)})
    m2 = Map({'a': Semigroup(3), 'b': Semigroup(4)})
    result = m1.concat(m2)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0.py .F         [100%]

=================================== FAILURES ===================================
____________________________ test_concat_same_keys _____________________________

    def test_concat_same_keys():
        m1 = Map({'a': Semigroup(1), 'b': Semigroup(2)})
        m2 = Map({'a': Semigroup(3), 'b': Semigroup(4)})
>       result = m1.concat(m2)

pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pyMonet/pymonet/semigroups.py:136: in concat
    {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <dict_itemiterator object at 0x7fba00320c70>

>       {key: value.concat(semigroup.value[key]) for key, value in self.value.items()}
    )
E   AttributeError: 'Semigroup' object has no attribute 'concat'

pyMonet/pymonet/semigroups.py:136: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_semigroups_Map_concat_0.py::test_concat_same_keys
========================= 1 failed, 1 passed in 0.06s ==========================
"""