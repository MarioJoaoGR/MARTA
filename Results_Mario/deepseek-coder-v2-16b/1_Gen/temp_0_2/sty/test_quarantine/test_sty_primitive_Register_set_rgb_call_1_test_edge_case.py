
import pytest
from sty import primitive

def test_set_rgb_call():
    reg = primitive.Register()
    
    # Mock a render type function
    def mock_render_func(r, g, b):
        return (r, g, b)
    
    # Set the RGB call to the mock function
    rendertype = type('RenderType', (), {'rgb': mock_render_func})
    reg.set_rgb_call(rendertype)
    
    # Check if rgb_call is set correctly
    assert reg.rgb_call(10, 42, 255) == (10, 42, 255)

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

sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________________ test_set_rgb_call _______________________________

    def test_set_rgb_call():
        reg = primitive.Register()
    
        # Mock a render type function
        def mock_render_func(r, g, b):
            return (r, g, b)
    
        # Set the RGB call to the mock function
        rendertype = type('RenderType', (), {'rgb': mock_render_func})
>       reg.set_rgb_call(rendertype)

sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_1_test_edge_case.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x106935360>
rendertype = <class 'Test4DT_tests.test_sty_primitive_Register_set_rgb_call_1_test_edge_case.RenderType'>

    def set_rgb_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(10, 42, 255)``
        is a RGB-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for RGB-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: <class 'Test4DT_tests.test_sty_primitive_Register_set_rgb_call_1_test_edge_case.RenderType'>

sty/sty/primitive.py:133: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_set_rgb_call_1_test_edge_case.py::test_set_rgb_call
============================== 1 failed in 0.02s ===============================
"""