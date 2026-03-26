
import pytest
from superstring.superstring import SuperStringBase

@pytest.mark.parametrize("start_index, end_index", [(None, None), (0, None), (None, 11), (3, 5)])
def test_edge_case_none_params(start_index, end_index):
    obj = SuperStringBase('Hello', 'World!')
    assert str(obj) == 'HelloWorld!'
    if start_index is not None and end_index is not None:
        assert str(obj)[start_index:end_index] == 'Hello'
    elif start_index is not None:
        assert len(str(obj)[start_index:]) == 5
    elif end_index is not None:
        assert len(str(obj)[:end_index]) == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
____________________ test_edge_case_none_params[None-None] _____________________

start_index = None, end_index = None

    @pytest.mark.parametrize("start_index, end_index", [(None, None), (0, None), (None, 11), (3, 5)])
    def test_edge_case_none_params(start_index, end_index):
>       obj = SuperStringBase('Hello', 'World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py:7: TypeError
______________________ test_edge_case_none_params[0-None] ______________________

start_index = 0, end_index = None

    @pytest.mark.parametrize("start_index, end_index", [(None, None), (0, None), (None, 11), (3, 5)])
    def test_edge_case_none_params(start_index, end_index):
>       obj = SuperStringBase('Hello', 'World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py:7: TypeError
_____________________ test_edge_case_none_params[None-11] ______________________

start_index = None, end_index = 11

    @pytest.mark.parametrize("start_index, end_index", [(None, None), (0, None), (None, 11), (3, 5)])
    def test_edge_case_none_params(start_index, end_index):
>       obj = SuperStringBase('Hello', 'World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py:7: TypeError
_______________________ test_edge_case_none_params[3-5] ________________________

start_index = 3, end_index = 5

    @pytest.mark.parametrize("start_index, end_index", [(None, None), (0, None), (None, 11), (3, 5)])
    def test_edge_case_none_params(start_index, end_index):
>       obj = SuperStringBase('Hello', 'World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py::test_edge_case_none_params[None-None]
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py::test_edge_case_none_params[0-None]
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py::test_edge_case_none_params[None-11]
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase___str___0_test_edge_case_none_params.py::test_edge_case_none_params[3-5]
============================== 4 failed in 0.05s ===============================
"""