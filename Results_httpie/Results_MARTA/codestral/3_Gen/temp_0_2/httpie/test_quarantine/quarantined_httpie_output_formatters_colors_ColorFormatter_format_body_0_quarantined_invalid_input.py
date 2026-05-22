
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import ColorFormatter

def test_format_body_invalid_mime():
    # Arrange
    color_formatter = ColorFormatter(env=None, explicit_json=False, color_scheme='default')
    
    # Act
    with patch('httpie.output.formatters.colors.get_lexer_for_mimetype', return_value=None):
        result = color_formatter.format_body("some body content", "invalid/mime")
    
    # Assert
    assert result == "some body content"

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
________________________ test_format_body_invalid_mime _________________________

    def test_format_body_invalid_mime():
        # Arrange
>       color_formatter = ColorFormatter(env=None, explicit_json=False, color_scheme='default')

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/colors.py:58: in __init__
    super().__init__(**kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.colors.ColorFormatter object at 0x7f7b223caa50>
kwargs = {}

    def __init__(self, **kwargs):
        """
        :param env: an class:`Environment` instance
        :param kwargs: additional keyword argument that some
                       formatters might require.
    
        """
        self.enabled = True
        self.kwargs = kwargs
>       self.format_options = kwargs['format_options']
E       KeyError: 'format_options'

httpie/httpie/plugins/base.py:140: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_format_body_0_test_invalid_input.py::test_format_body_invalid_mime
============================== 1 failed in 0.25s ===============================
"""