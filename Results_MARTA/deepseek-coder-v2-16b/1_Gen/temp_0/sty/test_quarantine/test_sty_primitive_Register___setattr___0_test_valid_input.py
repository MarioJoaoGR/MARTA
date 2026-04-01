
from sty.primitive import Register, Style, _render_rules

def test_valid_input():
    register = Register()
    style = Style([])  # Create a valid Style instance with empty rules
    
    # Set a valid Style instance to an attribute of the Register class
    register.__setattr__('test_attr', style)
    
    # Check if the test_attr has been set correctly in the register
    assert hasattr(register, 'test_attr')
    assert isinstance(getattr(register, 'test_attr'), Style)

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

sty/Test4DT_tests/test_sty_primitive_Register___setattr___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        register = Register()
        style = Style([])  # Create a valid Style instance with empty rules
    
        # Set a valid Style instance to an attribute of the Register class
>       register.__setattr__('test_attr', style)

sty/Test4DT_tests/test_sty_primitive_Register___setattr___0_test_valid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
sty/sty/primitive.py:80: in __setattr__
    rendered, rules = _render_rules(self.renderfuncs, value.rules)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

renderfuncs = {}, rules = ([],)

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

sty/sty/primitive.py:58: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register___setattr___0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.02s ===============================

"""