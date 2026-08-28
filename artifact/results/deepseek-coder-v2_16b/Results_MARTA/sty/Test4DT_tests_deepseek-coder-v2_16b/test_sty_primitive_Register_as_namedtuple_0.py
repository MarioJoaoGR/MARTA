
import pytest
from sty import primitive

# Fixture for creating a minimal instance of Register
@pytest.fixture
def create_minimal_register():
    return primitive.Register()

# Test scenarios
def test_valid_case(create_minimal_register):
    register = create_minimal_register
    assert not register.is_muted
    assert register.eightbit_call("test") == "test"
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

def test_edge_case():
    register = primitive.Register()
    assert not register.is_muted
    assert register.eightbit_call("test") == "test"
    assert register.rgb_call(10, 20, 30) == (10, 20, 30)

def test_invalid_input():
    with pytest.raises(TypeError):
        register = primitive.Register("invalid", "args")
