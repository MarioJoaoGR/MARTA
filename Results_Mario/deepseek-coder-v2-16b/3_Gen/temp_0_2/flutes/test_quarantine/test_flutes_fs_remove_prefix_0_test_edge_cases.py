
import pytest
from flutes.fs import remove_prefix

def test_edge_cases():
    # Test None input
    assert remove_prefix(None, "http") is None

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

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None input
>       assert remove_prefix(None, "http") is None

flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_edge_cases.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = None, prefix = 'http', fully_match = True

    def remove_prefix(s: str, prefix: str, fully_match: bool = True) -> str:
        r"""Remove the specified prefix from a string. If only parts of the prefix match and :attr:`fully_match` is
        ``False``, then only that part is removed.
    
        .. code:: python
    
            >>> remove_prefix("https://github.com/huzecong/flutes", "https://")
            "github.com/huzecong/flutes"
    
            >>> remove_prefix("preface", "prefix", fully_match=False)
            "face"
    
        :param s: The string whose prefix we want to remove.
        :param prefix: The prefix to remove.
        :param fully_match: If ``True``, the prefix is only removed if it fully matches. Defaults to ``False``.
        """
>       length = min(len(s), len(prefix))
E       TypeError: object of type 'NoneType' has no len()

flutes/flutes/fs.py:79: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_prefix_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""