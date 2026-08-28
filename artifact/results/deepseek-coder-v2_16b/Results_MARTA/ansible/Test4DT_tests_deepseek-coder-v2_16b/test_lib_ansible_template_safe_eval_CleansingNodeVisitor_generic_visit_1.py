
import ast
import builtins
import pytest

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

# Test scenarios
@pytest.fixture
def visitor():
    return CleansingNodeVisitor()

@pytest.fixture
def valid_node():
    return ast.parse('1 + 2').body[0]

@pytest.fixture
def edge_case_none():
    return None

@pytest.fixture
def invalid_node():
    return ast.parse('print(1)').body[0]

# Test functions
def test_valid_input(visitor, valid_node):
    with pytest.raises(Exception):
        visitor.generic_visit(valid_node)

def test_edge_case_none(visitor, edge_case_none):
    with pytest.raises(Exception):
        visitor.generic_visit(edge_case_none)

def test_invalid_input(visitor, invalid_node):
    with pytest.raises(Exception):
        visitor.generic_visit(invalid_node)
