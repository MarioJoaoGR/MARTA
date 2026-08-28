
import pytest
from sty.primitive import Register


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_custom_rgb_call _____________________________

    def test_custom_rgb_call():
        def my_rgb_call(r, g, b):
            return (r, g, b)
    
        register = Register()
>       register.set_rgb_call(my_rgb_call)

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___init___0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x7fed068c6d70>
rendertype = <function test_custom_rgb_call.<locals>.my_rgb_call at 0x7fed06a93ac0>

    def set_rgb_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(10, 42, 255)``
        is a RGB-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for RGB-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: <function test_custom_rgb_call.<locals>.my_rgb_call at 0x7fed06a93ac0>

/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/primitive.py:139: KeyError
_____________________________ test_export_as_dict ______________________________

    def test_export_as_dict():
        register = Register()
        register_dict = register.as_dict()
        expected_keys = {'is_muted', 'renderfuncs'}
>       assert set(register_dict.keys()) == expected_keys, "Exported dictionary should contain only is_muted and renderfuncs"
E       AssertionError: Exported dictionary should contain only is_muted and renderfuncs
E       assert set() == {'is_muted', 'renderfuncs'}
E         
E         Extra items in the right set:
E         'renderfuncs'
E         'is_muted'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___init___0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___init___0.py::test_custom_rgb_call
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___init___0.py::test_export_as_dict
============================== 2 failed in 0.04s ===============================
"""