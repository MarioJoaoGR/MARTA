
import pytest
from sty.primitive import Register, RenderType

def test_set_none_as_render_type():
    reg = Register()

    # Mock a render function to be set as None
    class MockRenderType:
        pass

    mock_func = lambda x: f"Mock {x}"

    # Set the mock function in the renderfuncs dictionary
    reg.renderfuncs[MockRenderType] = mock_func

    # Call set_eightbit_call with None, which should raise a TypeError
    with pytest.raises(TypeError):
        reg.set_eightbit_call(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_________________________ test_set_none_as_render_type _________________________

    def test_set_none_as_render_type():
        reg = Register()
    
        # Mock a render function to be set as None
        class MockRenderType:
            pass
    
        mock_func = lambda x: f"Mock {x}"
    
        # Set the mock function in the renderfuncs dictionary
        reg.renderfuncs[MockRenderType] = mock_func
    
        # Call set_eightbit_call with None, which should raise a TypeError
        with pytest.raises(TypeError):
>           reg.set_eightbit_call(None)

sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0_test_edge_case.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x101cb1810>, rendertype = None

    def set_eightbit_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(144)``
        is a Eightbit-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for Eightbit-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: None

sty/sty/primitive.py:123: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_set_eightbit_call_0_test_edge_case.py::test_set_none_as_render_type
============================== 1 failed in 0.02s ===============================

"""