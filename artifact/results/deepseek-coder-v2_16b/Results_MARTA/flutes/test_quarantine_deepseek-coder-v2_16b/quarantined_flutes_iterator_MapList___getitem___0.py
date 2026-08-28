
import pytest
from flutes.iterator import MapList

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_MapList___getitem___0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_empty _____________________________

    def test_edge_case_empty():
        def square(x):
            return x * x
    
        a = []
        mapped_a = MapList(square, a)
    
        with pytest.raises(TypeError):
>           _ = mapped_a[0]  # Attempting to access an element should raise TypeError

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_MapList___getitem___0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.MapList object at 0x7f0825629810>, item = 0

    def __getitem__(self, item):
        if isinstance(item, int):
>           return self.func(self.list[item])
E           IndexError: list index out of range

/opt/marta/baselines/codamosa/replication/test-apps/flutes/flutes/iterator.py:394: IndexError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_MapList___getitem___0.py::test_edge_case_empty
============================== 1 failed in 0.07s ===============================
"""