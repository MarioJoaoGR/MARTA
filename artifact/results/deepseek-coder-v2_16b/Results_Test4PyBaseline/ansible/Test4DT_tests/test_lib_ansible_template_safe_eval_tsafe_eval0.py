# Module: ansible.template.safe_eval
import pytest
import ast
import builtins
from types import SimpleNamespace

# Import the function from its module
from ansible.template.safe_eval import safe_eval

def test_basic_evaluation():
    result = safe_eval('1 + 2')
    assert result == 3

def test_expression_with_locals():
    locals_dict = {'a': 5, 'b': 3}
    result = safe_eval('a * b', locals=locals_dict)
    assert result == 15

def test_invalid_expression():
    with pytest.raises(Exception):
        safe_eval('1 / 0')

def test_include_exceptions():
    result, error = safe_eval('1 / 0', include_exceptions=True)
    assert result is None
    assert isinstance(error, ZeroDivisionError)

def test_jinja2_template_syntax():
    # Assuming you have a Jinja2 environment set up and the necessary filters/globals defined
    locals_dict = {'a': 5, 'b': 3}
    result = safe_eval('{{ a }} * {{ b }}', locals=locals_dict)
    assert result == 15

def test_invalid_expression_with_include_exceptions():
    result, error = safe_eval('invalid expression', include_exceptions=True)
    assert result == 'invalid expression'
    assert error is None

def test_builtin_function_call_in_local_scope():
    locals_dict = {'__builtins__': {}, 'print': print}
    with pytest.raises(Exception):
        safe_eval('print("Hello, World!")', locals=locals_dict)

if __name__ == "__main__":
    pytest.main()
