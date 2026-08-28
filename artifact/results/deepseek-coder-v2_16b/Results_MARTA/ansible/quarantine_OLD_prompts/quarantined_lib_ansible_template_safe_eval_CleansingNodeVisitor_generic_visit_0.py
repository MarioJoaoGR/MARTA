
import pytest
from unittest.mock import patch, MagicMock
from ansible.template.safe_eval import CleansingNodeVisitor
import ast
import builtins

# Define safe nodes and call enabled functions for testing
SAFE_NODES = [ast.BinOp, ast.Call, ast.Name]  # Example list of allowed AST node types
CALL_ENABLED = ['sin', 'cos']  # Example list of enabled function names for calls

class TestCleansingNodeVisitor:
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.visitor = CleansingNodeVisitor()
    
    def test_valid_expression(self):
        code_str = "1 + 2"
        node = ast.parse(code_str).body[0]
        with pytest.raises(Exception) as excinfo:
            self.visitor.generic_visit(node)
        assert str(excinfo.value) == "invalid expression (1 + 2)"
    
    @patch('builtins', {'sin': MagicMock(), 'cos': MagicMock()})
    def test_valid_function_call(self):
        code_str = "import math; math.sin(0)"
        node = ast.parse(code_str).body[0]
        with pytest.raises(Exception) as excinfo:
            self.visitor.generic_visit(node)
        assert str(excinfo.value) == "invalid function: sin"
    
    @patch('builtins', {'sin': MagicMock(), 'cos': MagicMock()})
    def test_valid_function_call_inside_module(self):
        module_code = """
        import math
        result = math.sin(0)
        """
        tree = ast.parse(module_code)
        with pytest.raises(Exception) as excinfo:
            self.visitor.generic_visit(tree)
        assert str(excinfo.value) == "invalid function: sin"
    
    @patch('builtins', {'sin': MagicMock(), 'cos': MagicMock()})
    def test_valid_function_call_inside_function(self):
        code_str = """
        import math
        def example():
            return math.sin(0)
        """
        tree = ast.parse(code_str)
        with pytest.raises(Exception) as excinfo:
            self.visitor.generic_visit(tree.body[0])
        assert str(excinfo.value) == "invalid function: sin"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting test_lib_ansible_template_safe_eval_CleansingNodeVisitor_generic_visit_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_safe_eval_CleansingNodeVisitor_generic_visit_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_safe_eval_CleansingNodeVisitor_generic_visit_0.py:4: in <module>
    from ansible.template.safe_eval import CleansingNodeVisitor
E   ImportError: cannot import name 'CleansingNodeVisitor' from 'ansible.template.safe_eval' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/template/safe_eval.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_template_safe_eval_CleansingNodeVisitor_generic_visit_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.59s ===============================
"""