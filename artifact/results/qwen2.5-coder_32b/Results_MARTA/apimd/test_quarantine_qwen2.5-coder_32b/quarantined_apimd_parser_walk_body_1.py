
import pytest
from ast import parse, If, Try, Assign, Expr
from typing import Sequence, Iterator
from apimd.parser import walk_body







"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 7 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py F [ 14%]
FFFFFF                                                                   [100%]

=================================== FAILURES ===================================
_______________________________ test_happy_path ________________________________

    def test_happy_path():
        source_code = """
    if x > 0:
        print('Positive')
    else:
        print('Non-positive')
    try:
        result = 1 / x
    except ZeroDivisionError:
        result = None
    finally:
        print('Done')
    """
        tree = parse(source_code.strip())
        nodes = list(walk_body(tree.body))
    
        # Asserting the number of statements yielded by walk_body
>       assert len(nodes) == 7
E       assert 5 == 7
E        +  where 5 = len([<ast.Expr object at 0x7f5e397613c0>, <ast.Expr object at 0x7f5e397600d0>, <ast.Assign object at 0x7f5e39761750>, <ast.Assign object at 0x7f5e39760f40>, <ast.Expr object at 0x7f5e39760ee0>])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:24: AssertionError
_________________________ test_invalid_input_handling __________________________

    def test_invalid_input_handling():
        invalid_body = [1, 2, 3]
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:29: Failed
_________________________ test_non_stmt_body_handling __________________________

    def test_non_stmt_body_handling():
        non_stmt_body = ['string', {}, []]
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:35: Failed
__________________________ test_if_statement_handling __________________________

    def test_if_statement_handling():
        source_code = """
    if x > 0:
        print('Positive')
    else:
        print('Non-positive')
    """
        tree = parse(source_code.strip())
        nodes = list(walk_body(tree.body))
    
        # Asserting the number of statements in an if-else block
>       assert len(nodes) == 3
E       assert 2 == 3
E        +  where 2 = len([<ast.Expr object at 0x7f5e397615a0>, <ast.Expr object at 0x7f5e39761c60>])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:49: AssertionError
_______________________ test_try_except_finally_handling _______________________

    def test_try_except_finally_handling():
        source_code = """
    try:
        result = 1 / x
    except ZeroDivisionError:
        result = None
    finally:
        print('Done')
    """
        tree = parse(source_code.strip())
        nodes = list(walk_body(tree.body))
    
        # Asserting the number of statements in a try-except-finally block
>       assert len(nodes) == 5
E       assert 3 == 5
E        +  where 3 = len([<ast.Assign object at 0x7f5e39766650>, <ast.Assign object at 0x7f5e39766740>, <ast.Expr object at 0x7f5e39766710>])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:64: AssertionError
___________________________ test_nested_if_handling ____________________________

    def test_nested_if_handling():
        source_code = """
    if x > 0:
        if y > 0:
            print('Both positive')
        else:
            print('x positive, y non-positive')
    else:
        print('x non-positive')
    """
        tree = parse(source_code.strip())
        nodes = list(walk_body(tree.body))
    
        # Asserting the number of statements in nested if-else blocks
>       assert len(nodes) == 5
E       assert 3 == 5
E        +  where 3 = len([<ast.Expr object at 0x7f5e39760550>, <ast.Expr object at 0x7f5e39613430>, <ast.Expr object at 0x7f5e39613670>])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:80: AssertionError
___________________________ test_nested_try_handling ___________________________

    def test_nested_try_handling():
        source_code = """
    try:
        try:
            result = 1 / x
        except ZeroDivisionError:
            result = None
    finally:
        print('Done')
    """
        tree = parse(source_code.strip())
        nodes = list(walk_body(tree.body))
    
        # Asserting the number of statements in nested try-except-finally blocks
>       assert len(nodes) == 6
E       assert 3 == 6
E        +  where 3 = len([<ast.Assign object at 0x7f5e397673a0>, <ast.Assign object at 0x7f5e39765630>, <ast.Expr object at 0x7f5e39765660>])

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py:96: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_invalid_input_handling
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_non_stmt_body_handling
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_if_statement_handling
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_try_except_finally_handling
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_nested_if_handling
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_qwen2.5-coder_32b/test_apimd_parser_walk_body_1.py::test_nested_try_handling
============================== 7 failed in 0.08s ===============================
"""