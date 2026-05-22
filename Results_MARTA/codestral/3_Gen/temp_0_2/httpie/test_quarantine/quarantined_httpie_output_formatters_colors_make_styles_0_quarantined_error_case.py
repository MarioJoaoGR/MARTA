
import pytest
from httpie.output.formatters.colors import make_styles

def test_make_styles():
    styles = make_styles()
    assert isinstance(styles, dict), "Expected a dictionary"
    for style in styles.values():
        assert len(style) == 2, "Each style should have both header and body"
        for s in style:
            assert isinstance(s, Style), f"Expected {type(Style)} but got {type(s)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_make_styles_0_test_error_case
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_styles_0_test_error_case.py:11:33: E0602: Undefined variable 'Style' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_styles_0_test_error_case.py:11:58: E0602: Undefined variable 'Style' (undefined-variable)


"""