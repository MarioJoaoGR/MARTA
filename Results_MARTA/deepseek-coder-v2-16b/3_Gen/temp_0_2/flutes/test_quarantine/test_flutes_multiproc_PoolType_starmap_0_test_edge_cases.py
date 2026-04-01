
import pytest
from flutes.multiproc import PoolType

def test_edge_cases():
    with pytest.raises(TypeError):
        pool = PoolType()
        pool.starmap(None, [(1, 2), (3, 4)])  # Providing a non-callable function should raise TypeError

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_edge_cases.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.22s ===============================
"""