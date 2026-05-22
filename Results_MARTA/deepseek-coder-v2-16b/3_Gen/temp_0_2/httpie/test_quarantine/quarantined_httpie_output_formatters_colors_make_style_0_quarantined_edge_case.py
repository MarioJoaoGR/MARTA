
import pytest
from httpie.output.formatters.colors import make_style
from pygments.token import Token

def test_make_style():
    raw_styles = {
        Token.Keyword: "bold red",
        Token.Number: "green"
    }
    
    MyStyle = make_style('MyStyle', raw_styles, 2)
    
    assert isinstance(MyStyle, type), "make_style should return a class instance"
    assert hasattr(MyStyle, 'styles'), "The custom style should have a 'styles' attribute"
    assert MyStyle.styles[Token.Keyword] == "bold red", "The keyword style should be 'bold red'"
    assert MyStyle.styles[Token.Number] == "green", "The number style should be 'green'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_make_style_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_make_style ________________________________

    def test_make_style():
        raw_styles = {
            Token.Keyword: "bold red",
            Token.Number: "green"
        }
    
>       MyStyle = make_style('MyStyle', raw_styles, 2)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_make_style_0_test_edge_case.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/colors.py:363: in make_style
    'styles': {
httpie/httpie/output/formatters/colors.py:364: in <dictcomp>
    key: format_value(value)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = 'bold red'

    def format_value(value):
>       return ' '.join(
            get_color(part, shade) or part
            for part in value.split()
        )
E       TypeError: sequence item 1: expected str instance, dict found

httpie/httpie/output/formatters/colors.py:356: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_make_style_0_test_edge_case.py::test_make_style
============================== 1 failed in 0.19s ===============================
"""