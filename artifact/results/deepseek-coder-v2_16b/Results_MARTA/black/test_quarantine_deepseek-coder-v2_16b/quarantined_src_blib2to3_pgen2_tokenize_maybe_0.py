
import pytest
import re
from blib2to3.pgen2.tokenize import maybe

@pytest.mark.parametrize("choices, expected", [
    (('apple', 'banana', 'cherry'), '(apple|banana|cherry)?'),
    ((), '()?'),
    ((None, 123, True), '()?')
])
def test_maybe(choices, expected):
    assert re.compile(maybe(*choices)).pattern == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_maybe_0.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
___________________________ test_maybe[choices2-()?] ___________________________

choices = (None, 123, True), expected = '()?'

    @pytest.mark.parametrize("choices, expected", [
        (('apple', 'banana', 'cherry'), '(apple|banana|cherry)?'),
        ((), '()?'),
        ((None, 123, True), '()?')
    ])
    def test_maybe(choices, expected):
>       assert re.compile(maybe(*choices)).pattern == expected

/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_maybe_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/black/src/blib2to3/pgen2/tokenize.py:71: in maybe
    return group(*choices) + "?"
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

choices = (None, 123, True)

    def group(*choices):
>       return "(" + "|".join(choices) + ")"
E       TypeError: sequence item 0: expected str instance, NoneType found

/opt/marta/baselines/codamosa/replication/test-apps/black/src/blib2to3/pgen2/tokenize.py:63: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_maybe_0.py::test_maybe[choices2-()?]
========================= 1 failed, 2 passed in 0.09s ==========================
"""