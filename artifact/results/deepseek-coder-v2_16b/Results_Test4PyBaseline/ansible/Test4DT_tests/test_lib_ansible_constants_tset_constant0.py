
# Module: ansible.constants
# test_set_constant.py
from ansible.constants import set_constant
import pytest

@pytest.fixture
def reset_globals():
    """ Reset the globals before each test to ensure no interference between tests """
    if 'PI' in vars():
        del vars()['PI']
    if 'TAX_RATE' in vars():
        del vars()['TAX_RATE']
    yield
    assert 'PI' not in vars()
    assert 'TAX_RATE' not in vars()

def test_set_constant_default(reset_globals):
    set_constant('PI', 3.14)
    assert 'PI' in vars()
    assert vars().get('PI') == 3.14

def test_set_constant_custom_dict(reset_globals):
    custom_dict = {}
    set_constant('TAX_RATE', 0.07, export=custom_dict)
    assert 'TAX_RATE' not in vars()
    assert custom_dict['TAX_RATE'] == 0.07

def test_set_constant_already_defined(reset_globals):
    if 'PI' not in vars():
        set_constant('PI', 3.14)
    assert 'PI' in vars()
    assert vars().get('PI') == 3.14
