
# Module: sty.primitive
# test_register.py
from sty.primitive import Register
import pytest

@pytest.fixture
def register():
    return Register()

def test_initialization(register):
    assert isinstance(register.renderfuncs, dict)
    assert register.is_muted is False
    assert callable(register.eightbit_call)
    assert callable(register.rgb_call)

def test_set_renderfunc(register):
    # Create a mock render function
    def mock_render_func(x):
        return f"Mock {x}"
    
    # Set the mock render function for a new RenderType instance
    class MockRenderType(Register.RenderType):
        pass
    
    rendertype = MockRenderType()
    register.set_renderfunc(rendertype, mock_render_func)
    
    assert len(register.renderfuncs) == 1
    assert isinstance(list(register.renderfuncs.keys())[0], type)
    assert list(register.renderfuncs.values())[0] == mock_render_func

def test_set_renderfunc_updates_style_attributes(register):
    # Create a mock Style class for testing attribute updates
    class MockStyle:
        pass
    
    # Add some style attributes to the register
    setattr(register, 'mock_style', MockStyle())
    
    def mock_render_func(x):
        return f"Mock {x}"
    
    class MockRenderType(Register.RenderType):
        pass
    
    rendertype = MockRenderType()
    register.set_renderfunc(rendertype, mock_render_func)
    
    # Check if the style attributes are updated correctly
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, MockStyle):
            assert hasattr(val, 'mock_style')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_set_renderfunc_0
sty/Test4DT_tests/test_sty_primitive_Register_set_renderfunc_0.py:23:25: E1101: Class 'Register' has no 'RenderType' member (no-member)
sty/Test4DT_tests/test_sty_primitive_Register_set_renderfunc_0.py:44:25: E1101: Class 'Register' has no 'RenderType' member (no-member)

"""