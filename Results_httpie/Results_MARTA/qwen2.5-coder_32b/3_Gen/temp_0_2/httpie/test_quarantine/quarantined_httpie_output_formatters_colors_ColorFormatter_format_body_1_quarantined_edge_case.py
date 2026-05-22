
import pytest
from httpie.output.formatters.colors import ColorFormatter
from unittest.mock import patch, MagicMock

@pytest.fixture
def color_formatter():
    env = MagicMock()
    env.colors = 256  # Assuming the environment supports colors for this test
    return ColorFormatter(env=env)

def test_format_body_with_lexer(color_formatter):
    with patch('httpie.output.formatters.colors.PygmentsHttpLexer') as mock_lexer, \
         patch('httpie.output.formatters.colors.TerminalFormatter') as mock_formatter:
        
        # Mock the lexer and formatter to avoid actual Pygments usage in this test
        mock_lexer.return_value = MagicMock()
        mock_formatter.return_value = MagicMock()
        
        body = "print('Hello, World!')"
        mime = 'text/x-python'  # Example MIME type for Python code
        
        result = color_formatter.format_body(body, mime)
        
        assert isinstance(result, str), "Expected the formatted body to be a string"
        mock_lexer.assert_called_once_with(precise=False)
        mock_formatter.return_value.highlight.assert_called_once_with(
            code=body, lexer=mock_lexer.return_value, formatter=mock_formatter.return_value
        )

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_ColorFormatter_format_body_1_test_edge_case.py E [100%]

==================================== ERRORS ====================================
________________ ERROR at setup of test_format_body_with_lexer _________________

    @pytest.fixture
    def color_formatter():
        env = MagicMock()
        env.colors = 256  # Assuming the environment supports colors for this test
>       return ColorFormatter(env=env)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_ColorFormatter_format_body_1_test_edge_case.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/colors.py:58: in __init__
    super().__init__(**kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.formatters.colors.ColorFormatter object at 0x7fc23d267e90>
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
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_ColorFormatter_format_body_1_test_edge_case.py::test_format_body_with_lexer
=============================== 1 error in 0.27s ===============================
"""