# Module: ansible.playbook.conditional
# test_conditional.py
from ansible.playbook.conditional import Conditional
import pytest

@pytest.fixture
def loader():
    # Create a mock loader for testing
    class MockLoader:
        pass
    return MockLoader()

@pytest.fixture
def templar():
    # Create a mock templar for testing
    class MockTemplar:
        def render(self, context):
            return context
    return MockTemplar()

@pytest.fixture
def all_vars():
    # Example variables for the test
    return {'some_var': 'value', 'some_condition': True}

def test_evaluate_conditional_all_true(loader, templar, all_vars):
    cond = Conditional()
    cond._when = ['{{ some_var == "value" }}', '{{ some_condition == True }}']
    assert cond.evaluate_conditional(templar=templar, all_vars=all_vars) is True

def test_evaluate_conditional_one_false(loader, templar, all_vars):
    cond = Conditional()
    cond._when = ['{{ some_var == "value" }}', '{{ some_condition == False }}']
    assert cond.evaluate_conditional(templar=templar, all_vars=all_vars) is False

def test_evaluate_conditional_empty(loader, templar, all_vars):
    cond = Conditional()
    cond._when = []
    assert cond.evaluate_conditional(templar=templar, all_vars=all_vars) is True

def test_evaluate_conditional_none(loader, templar, all_vars):
    cond = Conditional()
    cond._when = [None]
    assert cond.evaluate_conditional(templar=templar, all_vars=all_vars) is True

def test_evaluate_conditional_invalid_condition(loader, templar, all_vars):
    cond = Conditional()
    cond._when = ['{{ invalid_expression }}']
    with pytest.raises(AnsibleError):
        cond.evaluate_conditional(templar=templar, all_vars=all_vars)
