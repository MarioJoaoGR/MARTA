# Module: ansible.template.safe_eval
import ast
import builtins
import pytest

# Define safe nodes and allowed functions in calls
SAFE_NODES = {ast.Name, ast.Call}
CALL_ENABLED = {'allowed_function'}  # Replace with actual allowed functions

class CleansingNodeVisitor(ast.NodeVisitor):
    def generic_visit(self, node, inside_call=False):
        if type(node) not in SAFE_NODES:
            raise Exception("invalid expression (%s)" % expr)
        elif isinstance(node, ast.Call):
            inside_call = True
        elif isinstance(node, ast.Name) and inside_call:
            # Disallow calls to builtin functions that we have not vetted
            # as safe.  Other functions are excluded by setting locals in
            # the call to eval() later on
            if hasattr(builtins, node.id) and node.id not in CALL_ENABLED:
                raise Exception("invalid function: %s" % node.id)
        for child_node in ast.iter_child_nodes(node):
            self.generic_visit(child_node, inside_call)

# Test cases for valid AST nodes
def test_valid_ast_node():
    root_node = ast.parse("print('Hello, World!')")  # Creating an example AST
    visitor = CleansingNodeVisitor()
    with pytest.raises(Exception):
        visitor.visit(root_node)

# Test cases for invalid function call detection
def test_invalid_function_call():
    root_node = ast.parse("os._exit(0)")  # Creating an example AST with an unsafe function call
    visitor = CleansingNodeVisitor()
    with pytest.raises(Exception):
        visitor.visit(root_node)

# Test cases for handling nested nodes
def test_nested_nodes():
    root_node = ast.parse("os.path.join('dir', 'file')")  # Creating an example AST with nested function calls
    visitor = CleansingNodeVisitor()
    with pytest.raises(Exception):
        visitor.visit(root_node)
