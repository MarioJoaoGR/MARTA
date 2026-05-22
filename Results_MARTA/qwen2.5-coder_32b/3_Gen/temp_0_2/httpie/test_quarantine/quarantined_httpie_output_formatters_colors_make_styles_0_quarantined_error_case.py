
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import make_styles

def test_make_styles():
    with patch('httpie.output.formatters.colors.SHADE_TO_PIE_STYLE', {1: 'Light', 2: 'Dark'}), \
         patch('httpie.output.formatters.colors.PIE_HEADER_STYLE', {'Token.Keyword': "bold red", 'Token.Number': "green"}), \
         patch('httpie.output.formatters.colors.PIE_BODY_STYLE', {'Token.String': "blue", 'Token.Name': "purple"}):
         
        styles = make_styles()
        
        assert isinstance(styles, dict)
        assert len(styles) == 2
        for style in styles.values():
            assert isinstance(style, list) and len(style) == 2
            for s in style:
                assert isinstance(s, MagicMock)  # Assuming make_style returns a mock object

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_make_styles_0_test_error_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_make_styles _______________________________

    def test_make_styles():
        with patch('httpie.output.formatters.colors.SHADE_TO_PIE_STYLE', {1: 'Light', 2: 'Dark'}), \
             patch('httpie.output.formatters.colors.PIE_HEADER_STYLE', {'Token.Keyword': "bold red", 'Token.Number': "green"}), \
             patch('httpie.output.formatters.colors.PIE_BODY_STYLE', {'Token.String': "blue", 'Token.Name': "purple"}):
    
>           styles = make_styles()

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_make_styles_0_test_error_case.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/colors.py:375: in make_styles
    styles[name] = [
httpie/httpie/output/formatters/colors.py:376: in <listcomp>
    make_style(name, style_map, shade)
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
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_make_styles_0_test_error_case.py::test_make_styles
============================== 1 failed in 0.20s ===============================
"""