
import pytest
from typing import Any, Dict, Optional, Mapping
from unittest.mock import patch

def exec_in(code: Any, glob: Dict[str, Any], loc: Optional[Optional[Mapping[str, Any]]] = None) -> None:
    if isinstance(code, str):
        code = compile(code, "<string>", "exec", dont_inherit=True)
    exec(code, glob, loc)

@pytest.mark.parametrize("code, expected", [
    ('x = 5\ny = x + 3', {'x': 5, 'y': 8}),
])
def test_valid_code_execution(code: str, expected: Dict[str, Any]):
    global_scope = {}
    local_scope = {}
    exec_in(code, global_scope, local_scope)
    assert global_scope == expected

@pytest.mark.parametrize("code", [123])
def test_invalid_input(code: int):
    global_scope = {}
    local_scope = {}
    compiled_code = compile(str(code), "<string>", "exec")
    with pytest.raises(SyntaxError):
        exec_in(compiled_code, global_scope, local_scope)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________ test_valid_code_execution[x = 5\ny = x + 3-expected0] _____________

code = 'x = 5\ny = x + 3', expected = {'x': 5, 'y': 8}

    @pytest.mark.parametrize("code, expected", [
        ('x = 5\ny = x + 3', {'x': 5, 'y': 8}),
    ])
    def test_valid_code_execution(code: str, expected: Dict[str, Any]):
        global_scope = {}
        local_scope = {}
        exec_in(code, global_scope, local_scope)
>       assert global_scope == expected
E       AssertionError: assert {'__builtins_...ption'>, ...}} == {'x': 5, 'y': 8}
E         
E         Left contains 1 more item:
E         {'__builtins__': {'ArithmeticError': <class 'ArithmeticError'>,
E                           'AssertionError': <class 'AssertionError'>,
E                           'AttributeError': <class 'AttributeError'>,
E                           'BaseException': <class 'BaseException'>,
E                           'BlockingIOError': <class 'BlockingIOError'>,...
E         
E         ...Full output truncated (168 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py:18: AssertionError
___________________________ test_invalid_input[123] ____________________________

code = 123

    @pytest.mark.parametrize("code", [123])
    def test_invalid_input(code: int):
        global_scope = {}
        local_scope = {}
        compiled_code = compile(str(code), "<string>", "exec")
>       with pytest.raises(SyntaxError):
E       Failed: DID NOT RAISE <class 'SyntaxError'>

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py:25: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py::test_valid_code_execution[x = 5\ny = x + 3-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_util_exec_in_0.py::test_invalid_input[123]
============================== 2 failed in 0.07s ===============================
"""