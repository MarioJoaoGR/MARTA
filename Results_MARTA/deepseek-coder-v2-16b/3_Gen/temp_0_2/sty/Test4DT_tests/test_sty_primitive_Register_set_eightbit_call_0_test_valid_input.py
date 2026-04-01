
import pytest
from sty import primitive

@pytest.fixture
def register():
    return primitive.Register()

def test_valid_input(register):
    # Mock a render type for testing purposes
    class MockRenderType:
        pass

    # Define the mock function
    def mock_func(x):
        return x

    # Assign the mock function to the mock render type in the renderfuncs dictionary
    register.renderfuncs[MockRenderType] = mock_func

    # Call the set_eightbit_call method with the mock render type
    register.set_eightbit_call(MockRenderType)

    # Assert that the eightbit_call attribute of the register is now the mock function
    assert register.eightbit_call == mock_func
