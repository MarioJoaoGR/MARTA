
from flutes.fs import remove_suffix

def test_edge_case_none_input():
    assert remove_suffix(None, "suffix") is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_edge_case_none_input.py F [100%]

=================================== FAILURES ===================================
__________________________ test_edge_case_none_input ___________________________

    def test_edge_case_none_input():
>       assert remove_suffix(None, "suffix") is None

flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_edge_case_none_input.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = None, suffix = 'suffix', fully_match = True

    def remove_suffix(s: str, suffix: str, fully_match: bool = True) -> str:
        r"""Remove the specified suffix from a string. If only parts of the suffix match and :attr:`fully_match` is
        ``False``, then only that part is removed.
    
        .. code:: python
    
            >>> remove_suffix("https://github.com/huzecong/flutes", "/flutes")
            "https://github.com/huzecong"
    
            >>> remove_suffix("bugfix", "suffix", fully_match=False)
            "bug"
    
        :param s: The string whose suffix we want to remove.
        :param suffix: The suffix to remove.
        :param fully_match: If ``True``, the suffix is only removed if it fully matches. Defaults to ``False``.
        """
>       length = min(len(s), len(suffix))
E       TypeError: object of type 'NoneType' has no len()

flutes/flutes/fs.py:102: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_remove_suffix_1_test_edge_case_none_input.py::test_edge_case_none_input
============================== 1 failed in 0.10s ===============================
"""