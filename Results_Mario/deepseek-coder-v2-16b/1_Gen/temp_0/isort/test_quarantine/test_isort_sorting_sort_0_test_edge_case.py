
import pytest
from isort.sorting import sort
from isort import Config

def test_edge_case():
    config = None
    to_sort = []
    key_func = lambda x: len(x)
    
    # Test with None config
    with pytest.raises(TypeError):
        sort(config, to_sort, key=key_func, reverse=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_sorting_sort_0_test_edge_case.py F        [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        config = None
        to_sort = []
        key_func = lambda x: len(x)
    
        # Test with None config
        with pytest.raises(TypeError):
>           sort(config, to_sort, key=key_func, reverse=False)

isort/Test4DT_tests/test_isort_sorting_sort_0_test_edge_case.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

config = None, to_sort = []
key = <function test_edge_case.<locals>.<lambda> at 0x7f6748538f40>
reverse = False

    def sort(
        config: Config,
        to_sort: Iterable[str],
        key: Callable[[str], Any] | None = None,
        reverse: bool = False,
    ) -> list[str]:
>       return config.sorting_function(to_sort, key=key, reverse=reverse)
E       AttributeError: 'NoneType' object has no attribute 'sorting_function'

isort/isort/sorting.py:109: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting_sort_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.11s ===============================
"""