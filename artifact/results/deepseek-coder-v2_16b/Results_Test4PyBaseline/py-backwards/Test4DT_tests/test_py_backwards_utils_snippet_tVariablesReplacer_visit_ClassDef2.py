
import pytest
import ast
from py_backwards.utils.snippet import VariablesReplacer

# Helper function to create a Variable instance for testing
def create_variable(name, value):
    class Variable:
        def __init__(self, name: str, value: any):
            self.name = name
            self.value = value
    return Variable(name, value)

# Test replacing the 'name' field in a ClassDef node
def test_replace_classdef_name():
    class Node(ast.AST):
        _fields = ['name']
    
    variables_dict = {
        'original1': 'new_var1',
        'original2': create_variable('original2', None)
    }
    replacer = VariablesReplacer(variables_dict)
    
    node = ast.ClassDef(name='original1')
    replaced_node = replacer.visit_ClassDef(node)
    assert replaced_node.name == 'new_var1'

# Test replacing a field in an AST node with all_types=False for ClassDef
def test_replace_classdef_field_with_type_check():
    class Node(ast.AST):
        _fields = ['value']
    
    variables_dict = {
        'original1': create_variable('new_var1', None),
        'original2': create_variable('original2', None)
    }
    replacer = VariablesReplacer(variables_dict)
    
    node = ast.ClassDef()
    node.value = ast.Name(id='original2', ctx=ast.Load())
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=False)
    assert isinstance(replaced_node.value, ast.Name)
    assert replaced_node.value.id == 'original2'

# Test replacing a field in an AST node with all_types=True for ClassDef
def test_replace_classdef_field_with_all_types():
    class Node(ast.AST):
        _fields = ['value']
    
    variables_dict = {
        'original1': create_variable('new_var1', None),
        'original2': create_variable('original2', None)
    }
    replacer = VariablesReplacer(variables_dict)
    
    node = ast.ClassDef()
    node.value = ast.Name(id='original2', ctx=ast.Load())
    replaced_node = replacer._replace_field_or_node(node, 'value', all_types=True)
    assert isinstance(replaced_node.value, ast.Name)