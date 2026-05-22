
import textwrap
from unittest.mock import patch
from httpie.cli.definition import BUNDLED_STYLES, DEFAULT_STYLE, AUTO_STYLE

def format_style_help(available_styles, *, isolation_mode: bool = False):
    """
    Generate a help text for available styles based on the provided list and optional isolation mode.

    Parameters:
        available_styles (list): A list of available color styles that can be used in the output.
        isolation_mode (bool, optional): If True, include additional instructions for finding out all available styles in the system. Defaults to False.

    Returns:
        str: A formatted help text string detailing the available styles and any specific requirements or notes related to them.
    """
    text = f"""
    Output coloring style (default is "{DEFAULT_STYLE}"). It can be one of:

        {available_styles_text}
    """
    if isolation_mode:
        text += '\n\n'
        text += 'For finding out all available styles in your system, try:\n\n'
        text += '    $ http --style\n'
    text += textwrap.dedent("""
        The "{auto_style}" style follows your terminal's ANSI color styles.
        For non-{auto_style} styles to work properly, please make sure that the
        $TERM environment variable is set to "xterm-256color" or similar
        (e.g., via `export TERM=xterm-256color' in your ~/.bashrc).
    """)

    if isolation_mode:
        available_styles = sorted(BUNDLED_STYLES)

    available_styles_text = '\n'.join(
        f'    {line.strip()}'
        for line in textwrap.wrap(', '.join(available_styles), 60)
    ).strip()
    return text.format(
        default=DEFAULT_STYLE,
        available_styles=available_styles_text,
        auto_style=AUTO_STYLE,
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_cli_definition_format_style_help_0_test_edge_case_none
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_definition_format_style_help_0_test_edge_case_none.py:20:9: E0601: Using variable 'available_styles_text' before assignment (used-before-assignment)


"""