
import pytest
import ast
from thonny.jedi_utils import get_statement_of_position

@pytest.mark.parametrize("code, expected_line, expected_column", [
    ("print('Hello, World!')", 1, 0),
    ("if True:\n    print('Inside if')", 2, 4)
])
def test_get_statement_of_position(code, expected_line, expected_column):
    node = ast.parse(code)
    statement = get_statement_of_position(node, (expected_line, expected_column))
    
    assert isinstance(statement, jedi.Statement), "Expected a jedi.Statement object"
    assert statement.start_pos == (expected_line - 1, expected_column), f"Unexpected start position: {statement.start_pos}"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________ test_get_statement_of_position[print('Hello, World!')-1-0] __________

code = "print('Hello, World!')", expected_line = 1, expected_column = 0

    @pytest.mark.parametrize("code, expected_line, expected_column", [
        ("print('Hello, World!')", 1, 0),
        ("if True:\n    print('Inside if')", 2, 4)
    ])
    def test_get_statement_of_position(code, expected_line, expected_column):
        node = ast.parse(code)
>       statement = get_statement_of_position(node, (expected_line, expected_column))

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:16: in get_statement_of_position
    return func(node, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = <ast.Module object at 0x7fb692514430>, pos = (1, 0)

    def _copy_of_get_statement_of_position(node, pos):
        # https://github.com/davidhalter/jedi/commit/9f3a2f93c48eda24e2dcc25e54eb7cc10aa73848
        from parso.python import tree
    
>       for c in node.children:
E       AttributeError: 'Module' object has no attribute 'children'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:24: AttributeError
_____ test_get_statement_of_position[if True:\n    print('Inside if')-2-4] _____

code = "if True:\n    print('Inside if')", expected_line = 2
expected_column = 4

    @pytest.mark.parametrize("code, expected_line, expected_column", [
        ("print('Hello, World!')", 1, 0),
        ("if True:\n    print('Inside if')", 2, 4)
    ])
    def test_get_statement_of_position(code, expected_line, expected_column):
        node = ast.parse(code)
>       statement = get_statement_of_position(node, (expected_line, expected_column))

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:16: in get_statement_of_position
    return func(node, pos)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

node = <ast.Module object at 0x7fb692073dc0>, pos = (2, 4)

    def _copy_of_get_statement_of_position(node, pos):
        # https://github.com/davidhalter/jedi/commit/9f3a2f93c48eda24e2dcc25e54eb7cc10aa73848
        from parso.python import tree
    
>       for c in node.children:
E       AttributeError: 'Module' object has no attribute 'children'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/jedi_utils.py:24: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py::test_get_statement_of_position[print('Hello, World!')-1-0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py::test_get_statement_of_position[if True:\n    print('Inside if')-2-4]
============================== 2 failed in 0.14s ===============================
"""