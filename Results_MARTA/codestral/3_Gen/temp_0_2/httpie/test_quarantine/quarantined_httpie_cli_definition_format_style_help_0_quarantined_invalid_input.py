
import pytest
from unittest.mock import patch
from httpie.cli.definition import BUNDLED_STYLES, DEFAULT_STYLE, AUTO_STYLE

def format_style_help(available_styles, *, isolation_mode: bool = False):
    text = """
    Output coloring style (default is "{default}"). It can be one of:

        {available_styles}
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

@pytest.mark.parametrize("isolation_mode", [True, False])
def test_invalid_input(isolation_mode):
    with patch('httpie.cli.definition.BUNDLED_STYLES', ['plain', 'colorful']):
        with patch('httpie.cli.definition.DEFAULT_STYLE', 'plain'):
            with patch('httpie.cli.definition.AUTO_STYLE', 'auto_style'):
                expected_text = """
                Output coloring style (default is "plain"). It can be one of:
                    
                    plain
                    colorful
                
                The "auto_style" style follows your terminal's ANSI color styles.
                For non-auto_style styles to work properly, please make sure that the
                $TERM environment variable is set to "xterm-256color" or similar
                (e.g., via `export TERM=xterm-256color' in your ~/.bashrc).
                """
                if isolation_mode:
                    expected_text += '\n\nFor finding out all available styles in your system, try:\n\n    $ http --style\n'
                
                assert format_style_help(['plain', 'colorful'], isolation_mode=isolation_mode) == expected_text.strip()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_cli_definition_format_style_help_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_cli_definition_format_style_help_0_test_invalid_input.py:16:12: E0602: Undefined variable 'textwrap' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_cli_definition_format_style_help_0_test_invalid_input.py:28:20: E0602: Undefined variable 'textwrap' (undefined-variable)


"""