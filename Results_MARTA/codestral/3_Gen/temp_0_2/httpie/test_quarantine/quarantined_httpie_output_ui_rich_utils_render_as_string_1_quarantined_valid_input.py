
import os
from rich.console import Console
from rich.render import RenderableType
from unittest.mock import patch

def render_as_string(renderable: RenderableType) -> str:
    """Render any `rich` object in a fake console and return a *style-less* version of it as a string."""
    
    with open(os.devnull, 'w') as null_stream:
        with patch('httpie.output.ui.rich_utils._make_rich_color_theme', return_value=None):
            fake_console = Console(file=null_stream, record=True)
            fake_console.print(renderable)
            return fake_console.export_text()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_ui_rich_utils_render_as_string_1_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_render_as_string_1_test_valid_input.py:4:0: E0401: Unable to import 'rich.render' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_ui_rich_utils_render_as_string_1_test_valid_input.py:4:0: E0611: No name 'render' in module 'rich' (no-name-in-module)


"""