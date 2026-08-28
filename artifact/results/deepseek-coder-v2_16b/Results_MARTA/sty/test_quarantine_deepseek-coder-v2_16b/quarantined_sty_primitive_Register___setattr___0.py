
import pytest
from sty.primitive import Register, Style




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_setattr_with_style ____________________________

    def test_setattr_with_style():
        class StylingRule: pass
        rules = [StylingRule()]
        style = Style(rules)
        register = Register()
>       setattr(register, 'fg', style)

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/primitive.py:85: in __setattr__
    rendered, rules = _render_rules(self.renderfuncs, value.rules)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

renderfuncs = {}
rules = ([<test_sty_primitive_Register___setattr___0.test_setattr_with_style.<locals>.StylingRule object at 0x7fba411fb010>],)

    def _render_rules(
        renderfuncs: Renderfuncs,
        rules: Iterable[StylingRule],
    ) -> Tuple[str, Iterable[StylingRule]]:
    
        rendered: str = ""
        flattened_rules: List[StylingRule] = []
    
        for rule in rules:
    
            if isinstance(rule, RenderType):
                f1: Callable = renderfuncs[type(rule)]
                rendered += f1(*rule.args)
                flattened_rules.append(rule)
    
            elif isinstance(rule, Style):
                r1, r2 = _render_rules(renderfuncs, rule.rules)
                rendered += r1
                flattened_rules.extend(r2)
    
            else:
>               raise ValueError("Parameter 'rules' must be of type Iterable[Rule].")
E               ValueError: Parameter 'rules' must be of type Iterable[Rule].

/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/primitive.py:61: ValueError
_________________________ test_setattr_with_non_style __________________________

    def test_setattr_with_non_style():
        register = Register()
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py:16: Failed
______________________________ test_set_rgb_call _______________________________

    def test_set_rgb_call():
        def my_rgb_call(r, g, b):
            return (r, g, b)
    
        register = Register()
>       register.set_rgb_call(my_rgb_call)

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <sty.primitive.Register object at 0x7fba410a5240>
rendertype = <function test_set_rgb_call.<locals>.my_rgb_call at 0x7fba4106fc70>

    def set_rgb_call(self, rendertype: Type[RenderType]) -> None:
        """
        You can call a register-object directly. A call like this ``fg(10, 42, 255)``
        is a RGB-call. With this method you can define the render-type for such calls.
    
        :param rendertype: The new rendertype that is used for RGB-calls.
        """
>       func: Callable = self.renderfuncs[rendertype]
E       KeyError: <function test_set_rgb_call.<locals>.my_rgb_call at 0x7fba4106fc70>

/opt/marta/baselines/codamosa/replication/test-apps/sty/sty/primitive.py:139: KeyError
_________________________________ test_as_dict _________________________________

    def test_as_dict():
        register = Register()
        register_dict = register.as_dict()
        expected_keys = {'renderfuncs', 'is_muted', 'eightbit_call', 'rgb_call'}
>       assert set(register_dict.keys()) == expected_keys
E       AssertionError: assert set() == {'eightbit_ca...', 'rgb_call'}
E         
E         Extra items in the right set:
E         'eightbit_call'
E         'is_muted'
E         'renderfuncs'
E         'rgb_call'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py:33: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py::test_setattr_with_style
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py::test_setattr_with_non_style
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py::test_set_rgb_call
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sty/Test4DT_tests_deepseek-coder-v2_16b/test_sty_primitive_Register___setattr___0.py::test_as_dict
============================== 4 failed in 0.06s ===============================
"""