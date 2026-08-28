
import pytest
from flutes.iterator import Range


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___next___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        r = Range(10)
        assert list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
        r = Range(1, 10 + 1)
>       assert list(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
E       assert [1, 2, 3, 4, 5, 6, ...] == [1, 2, 3, 4, 5, 6, ...]
E         
E         Left contains one more item: 10
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___next___0.py:10: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
>           r = Range("string")

/opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___next___0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.Range object at 0x7fbed562fd00>, args = ('string',)

    def __init__(self, *args):
        if len(args) == 0 or len(args) > 3:
            raise ValueError("Range should be called the same way as the builtin `range`")
        if len(args) == 1:
            self.l = 0
            self.r = args[0]
            self.step = 1
        else:
            self.l = args[0]
            self.r = args[1]
            self.step = 1 if len(args) == 2 else args[2]
        self.val = self.l
>       self.length = (self.r - self.l) // self.step
E       TypeError: unsupported operand type(s) for -: 'str' and 'int'

/opt/marta/baselines/codamosa/replication/test-apps/flutes/flutes/iterator.py:328: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___next___0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutes/Test4DT_tests_deepseek-coder-v2_16b/test_flutes_iterator_Range___next___0.py::test_invalid_inputs
============================== 2 failed in 0.08s ===============================
"""