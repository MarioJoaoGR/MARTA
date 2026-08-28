
import pytest

def needs_parentheses(source):
    def code(s):
        return compile(s, '<variable>', 'eval').co_code

    try:
        return code('{}.x'.format(source)) != code('({}).x'.format(source))
    except SyntaxError:
        return False

def test_happy_path_simple_expression():
    assert needs_parentheses('1 + 2') == False

def test_happy_path_or_operator():
    assert needs_parentheses('a or b') == True

def test_happy_path_nested_expression():
    assert needs_parentheses('a and (b or c)') == True

def test_happy_path_function_calls():
    assert needs_parentheses('f() or g()') == True

def test_happy_path_method_call():
    assert needs_parentheses('obj.method()') == False

def test_edge_case_empty_string():
    assert needs_parentheses('') == False

def test_edge_case_single_variable():
    assert needs_parentheses('a') == False

def test_edge_case_parenthesized_expression():
    assert needs_parentheses('(a or b)') == False

def test_edge_case_parenthesized_nested_expression():
    assert needs_parentheses('(a and (b or c))') == False

def test_edge_case_parenthesized_function_calls():
    assert needs_parentheses('(f() or g())') == False
