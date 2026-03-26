
import pytest
from flutes.network import download
import os
import tempfile
import tarfile
import zipfile
from functools import partial
from tqdm import tqdm

@pytest.mark.parametrize("params", [
    ({'url': None, 'save_dir': None, 'filename': None, 'extract': False, 'progress': False, 'bar_fn': None})
])
def test_edge_case_none(params):
    with pytest.raises(TypeError) as excinfo:
        download(**params)
    assert "missing 1 required positional argument" in str(excinfo.value)

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

flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_________________________ test_edge_case_none[params0] _________________________

params = {'bar_fn': None, 'extract': False, 'filename': None, 'progress': False, ...}

    @pytest.mark.parametrize("params", [
        ({'url': None, 'save_dir': None, 'filename': None, 'extract': False, 'progress': False, 'bar_fn': None})
    ])
    def test_edge_case_none(params):
        with pytest.raises(TypeError) as excinfo:
            download(**params)
>       assert "missing 1 required positional argument" in str(excinfo.value)
E       assert 'missing 1 required positional argument' in "argument of type 'NoneType' is not iterable"
E        +  where "argument of type 'NoneType' is not iterable" = str(TypeError("argument of type 'NoneType' is not iterable"))
E        +    where TypeError("argument of type 'NoneType' is not iterable") = <ExceptionInfo TypeError("argument of type 'NoneType' is not iterable") tblen=2>.value

flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py::test_edge_case_none[params0]
============================== 1 failed in 0.10s ===============================
"""