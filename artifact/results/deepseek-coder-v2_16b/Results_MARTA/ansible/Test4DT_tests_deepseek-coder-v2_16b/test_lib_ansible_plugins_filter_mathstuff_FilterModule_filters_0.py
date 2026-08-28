
import pytest
from ansible.plugins.filter import mathstuff

@pytest.fixture
def filter_module():
    return mathstuff.FilterModule()



def test_invalid_inputs(filter_module):
    filters = filter_module.filters()
    with pytest.raises(TypeError):
        filters['min']("not a list")
    with pytest.raises(TypeError):
        filters['max'](42)
    with pytest.raises(TypeError):
        filters['log']("logarithm")
    with pytest.raises(TypeError):
        filters['pow']("power", 3)