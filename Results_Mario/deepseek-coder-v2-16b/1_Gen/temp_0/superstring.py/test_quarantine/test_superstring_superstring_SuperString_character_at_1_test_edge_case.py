
from superstring.superstring import SuperString
import pytest

def test_edge_case():
    superstring = SuperString('Hello, World!')
    
    # Test for None index
    with pytest.raises(IndexError):
        assert superstring.character_at(None) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        superstring = SuperString('Hello, World!')
    
        # Test for None index
        with pytest.raises(IndexError):
>           assert superstring.character_at(None) is None

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_1_test_edge_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperString object at 0x7fe3fde3e910>
index = None

    def character_at(self, index):
>       return self._content[index]
E       TypeError: string indices must be integers, not 'NoneType'

superstring.py/superstring/superstring.py:86: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString_character_at_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.05s ===============================
"""