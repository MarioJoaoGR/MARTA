
import ast
import builtins
import pytest
from unittest.mock import patch

# Assuming SAFE_NODES and CALL_ENABLED are defined elsewhere in your codebase
SAFE_NODES = [...]  # List of allowed AST node types
CALL_ENABLED = [...]  # List of enabled function names for calls

class CleansingNodeVisitor:
    def generic_visit(self, node, inside_call=False):
        if type(node) not in SAFE_NODES:
            raise Exception("invalid expression (%s)" % expr)
        elif isinstance(node, ast.Call):
            inside_call = True
        elif isinstance(node, ast.Name) and inside_call:
            # Disallow calls to builtin functions that we have not vetted as safe.
            if hasattr(builtins, node.id) and node.id not in CALL_ENABLED:
                raise Exception("invalid function: %s" % node.id)
        for child_node in ast.iter_child_nodes(node):
            self.generic_visit(child_node, inside_call)

@pytest.fixture
def visitor():
    return CleansingNodeVisitor()

# Test scenarios

@pytest.mark.parametrize("code_str", ["1 + 2"])
def test_valid_input(visitor, code_str):
    node = ast.parse(code_str).body[0]
    with pytest.raises(Exception) as excinfo:
        visitor.generic_visit(node)
    assert "invalid expression" in str(excinfo.value)

def test_edge_case_none(visitor):
    node = None
    with pytest.raises(Exception) as excinfo:
        visitor.generic_visit(node)
    assert "invalid expression" in str(excinfo.value)

@pytest.mark.parametrize("code_str", ["print(1)"])
def test_invalid_input(visitor, code_str):
    node = ast.parse(code_str).body[0]
    with pytest.raises(Exception) as excinfo:
        visitor.generic_visit(node)
    assert "invalid function" in str(excinfo.value)
