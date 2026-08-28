
import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer

class Variable:
    def __init__(self, value):
        self.value = value



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_replace_in_dictionary __________________________

    def test_replace_in_dictionary():
        variables_dict = {
            'x': Variable(10),
            'y': Variable(20)
        }
    
        replacer = VariablesReplacer(variables_dict)
        replaced_data = replacer._replace_field_or_node({'x': 1, 'y': 2}, 'x')
>       assert replaced_data == {'uniqueVar1': 1, 'y': 2}
E       AssertionError: assert {'x': 1, 'y': 2} == {'uniqueVar1': 1, 'y': 2}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 1 more item:
E         {'x': 1}
E         Right contains 1 more item:
E         {'uniqueVar1': 1}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py:18: AssertionError
_____________________________ test_replace_in_ast ______________________________

    def test_replace_in_ast():
        variables_dict = {
            'x': Variable(10),
            'y': Variable(20)
        }
    
        replacer = VariablesReplacer(variables_dict)
        sample_ast = ast.parse("def example_function(): x = 10; y = x + 5")
        modified_tree = replacer.replace(tree=sample_ast, variables=variables_dict)
>       assert [node.__class__.__name__ for node in modified_tree.body[0].body] == ['Assign', 'Expr', 'Name']
E       AssertionError: assert ['Assign', 'Assign'] == ['Assign', 'Expr', 'Name']
E         
E         At index 1 diff: 'Assign' != 'Expr'
E         Right contains one more item: 'Name'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py:29: AssertionError
_____________________________ test_replace_method ______________________________

    def test_replace_method():
        class Variable:
            def __init__(self, value):
                self.value = value
    
        variables_dict = {
            'x': Variable(10),
            'y': Variable(20)
        }
    
>       modified_tree = VariablesReplacer.replace(cls=VariablesReplacer, tree=ast.parse("def example_function(): x = 10; y = x + 5"), variables=variables_dict)
E       TypeError: VariablesReplacer.replace() got multiple values for argument 'cls'

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py:41: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py::test_replace_in_dictionary
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py::test_replace_in_ast
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_snippet_VariablesReplacer_replace_0.py::test_replace_method
============================== 3 failed in 0.07s ===============================
"""