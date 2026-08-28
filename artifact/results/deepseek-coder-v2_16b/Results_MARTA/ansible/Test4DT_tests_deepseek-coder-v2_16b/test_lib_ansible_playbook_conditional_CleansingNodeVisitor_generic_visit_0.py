
import ast
from your_module import CleansingNodeVisitor
import pytest
from ansible.playbook.conditional import AnsibleError

# Test Scenario 1: Inside a Function Call
def test_valid_case_inside_call():
    code_str = 'some_expression'
    node = ast.parse(code_str).body[0]
    cnv = CleansingNodeVisitor()
    with pytest.raises(AnsibleError):
        cnv.generic_visit(node, inside_call=True)

# Test Scenario 2: Inside a Yield Expression
def test_valid_case_inside_yield():
    code_str = 'yield some_expression'
    node = ast.parse(code_str).body[0]
    cnv = CleansingNodeVisitor()
    with pytest.raises(AnsibleError):
        cnv.generic_visit(node, inside_yield=True)

# Test Scenario 3: Invalid Access in Conditional Statement or Yield Expression
def test_error_case_invalid_access():
    code_str = 'if __name__ == "__main__": pass'
    node = ast.parse(code_str).body[0]
    cnv = CleansingNodeVisitor()
    with pytest.raises(AnsibleError):
        cnv.generic_visit(node)
