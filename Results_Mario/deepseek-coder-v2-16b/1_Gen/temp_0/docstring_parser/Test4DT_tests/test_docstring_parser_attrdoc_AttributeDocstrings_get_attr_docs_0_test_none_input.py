
import ast
import inspect
import textwrap
from typing import Any, Dict, Optional, Tuple
import pytest
from unittest.mock import patch

class AttributeDocstrings:
    """An ast.NodeVisitor that collects attribute docstrings."""
    attr_docs = None
    prev_attr = None
    
    def get_attr_docs(self, component: Any) -> Dict[str, Tuple[str, Optional[str], Optional[str]]]:
        """Get attribute docstrings from the given component.

        :param component: component to process (class or module)
        :returns: for each attribute docstring, a tuple with (description, type, default)
        """
        self.attr_docs = {}
        self.prev_attr = None
        try:
            source = textwrap.dedent(inspect.getsource(component))
        except OSError:
            pass
        else:
            tree = ast.parse(source)
            if inspect.ismodule(component):
                self.visit(tree)
            elif isinstance(tree, ast.Module) and isinstance(tree.body[0], ast.ClassDef):
                self.visit(tree.body[0])
        return self.attr_docs
    
    def visit_Attribute(self, node):
        if isinstance(node.ctx, ast.Load):
            attr_name = node.attr
            if attr_name not in self.attr_docs:
                self.attr_docs[attr_name] = (None, None, None)
    
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Attribute):
                attr_name = target.attr
                if attr_name not in self.attr_docs:
                    self.attr_docs[attr_name] = (None, None, None)
    
    def visit_ClassDef(self, node):
        for stmt in node.body:
            if isinstance(stmt, ast.Assign):
                self.visit_Assign(stmt)
            elif isinstance(stmt, ast.FunctionDef) or isinstance(stmt, ast.AsyncFunctionDef):
                pass  # Skip function definitions
    
    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        raise RuntimeError(f"No visit_{node.__class__.__name__} method")

@pytest.fixture
def visitor():
    return AttributeDocstrings()

@pytest.mark.parametrize("component", [None])
def test_none_input(visitor, component):
    with pytest.raises(TypeError):
        attr_docs = visitor.get_attr_docs(component)
