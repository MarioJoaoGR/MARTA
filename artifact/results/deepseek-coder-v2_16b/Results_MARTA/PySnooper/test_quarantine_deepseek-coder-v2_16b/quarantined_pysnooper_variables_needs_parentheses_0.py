
import pytest
from pysnooper.variables import needs_parentheses

# Test cases for needs_parentheses function
@pytest.mark.parametrize("source, expected", [
    ('2 + 3', True),
    ('x = 5', False),
    ('a and b or c', True),
    ('(2 + 3)', False),
    (None, None)
])
def test_needs_parentheses(source, expected):
    if source is None:
        with pytest.raises(TypeError):
            needs_parentheses(source)
    else:
        assert needs_parentheses(source) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py F [ 20%]
F..F                                                                     [100%]

=================================== FAILURES ===================================
______________________ test_needs_parentheses[2 + 3-True] ______________________

source = '2 + 3', expected = True

    @pytest.mark.parametrize("source, expected", [
        ('2 + 3', True),
        ('x = 5', False),
        ('a and b or c', True),
        ('(2 + 3)', False),
        (None, None)
    ])
    def test_needs_parentheses(source, expected):
        if source is None:
            with pytest.raises(TypeError):
                needs_parentheses(source)
        else:
>           assert needs_parentheses(source) == expected

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:17: in needs_parentheses
    return code('{}.x'.format(source)) != code('({}).x'.format(source))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = '2 + 3.x'

    def code(s):
>       return compile(s, '<variable>', 'eval').co_code
E         File "<variable>", line 1
E           2 + 3.x
E                ^
E       SyntaxError: invalid decimal literal

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:15: SyntaxError
_____________________ test_needs_parentheses[x = 5-False] ______________________

source = 'x = 5', expected = False

    @pytest.mark.parametrize("source, expected", [
        ('2 + 3', True),
        ('x = 5', False),
        ('a and b or c', True),
        ('(2 + 3)', False),
        (None, None)
    ])
    def test_needs_parentheses(source, expected):
        if source is None:
            with pytest.raises(TypeError):
                needs_parentheses(source)
        else:
>           assert needs_parentheses(source) == expected

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:17: in needs_parentheses
    return code('{}.x'.format(source)) != code('({}).x'.format(source))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

s = 'x = 5.x'

    def code(s):
>       return compile(s, '<variable>', 'eval').co_code
E         File "<variable>", line 1
E           x = 5.x
E                ^
E       SyntaxError: invalid decimal literal

/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/variables.py:15: SyntaxError
______________________ test_needs_parentheses[None-None] _______________________

source = None, expected = None

    @pytest.mark.parametrize("source, expected", [
        ('2 + 3', True),
        ('x = 5', False),
        ('a and b or c', True),
        ('(2 + 3)', False),
        (None, None)
    ])
    def test_needs_parentheses(source, expected):
        if source is None:
>           with pytest.raises(TypeError):
E           Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py::test_needs_parentheses[2 + 3-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py::test_needs_parentheses[x = 5-False]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_variables_needs_parentheses_0.py::test_needs_parentheses[None-None]
========================= 3 failed, 2 passed in 0.06s ==========================
"""