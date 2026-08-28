
import pytest
from apimd.parser import const_type, Constant, Tuple, List, Set, Dict, Call, Name, Attribute
from ast import unparse
from itertools import chain
from typing import Optional

# Helper function to determine the type name of a constant value
def _type_name(value):
    if isinstance(value, bool):
        return 'bool'
    elif isinstance(value, int):
        return 'int'
    elif isinstance(value, float):
        return 'float'
    elif isinstance(value, complex):
        return 'complex'
    elif isinstance(value, str):
        return 'str'
    else:
        return 'ANY'

# Helper function to determine the element type of a collection (tuple, list, set)
def _e_type(elements, *args):
    types = {type(el).__name__.lower() for el in elements}
    if len(types) == 1:
        return '[' + next(iter(types)) + ']'
    else:
        return '[ANY]'

# Test cases for const_type function


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        assert const_type(Constant(1)) == 'int'
        assert const_type(Tuple([Constant(1), Constant(2)])) == 'tuple[int]'
>       assert const_type(List([Constant('a'), Constant(1)])) == 'list[ANY]'
E       AssertionError: assert 'list[Any]' == 'list[ANY]'
E         
E         - list[ANY]
E         ?       ^^
E         + list[Any]
E         ?       ^^

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py:35: AssertionError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
>       assert const_type(None) == 'ANY'
E       AssertionError: assert 'Any' == 'ANY'
E         
E         - ANY
E         + Any

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py:41: AssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py:44: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_const_type_0.py::test_invalid_inputs
============================== 3 failed in 0.06s ===============================
"""