
import sys
from isort.format import BasicPrinter, ColoramaPrinter

def create_terminal_printer(
    color: bool, output: TextIO | None = None, error: str = "", success: str = ""
) -> BasicPrinter:
    """
    Creates a terminal printer that can print text with specific colors for errors and successes. The function initializes the Colorama library if color is enabled to support ANSI color codes. If colorama is unavailable, it prints an error message and exits.
    
    Parameters:
        color (bool): A flag indicating whether to enable color output. If True, the printer will use colors for errors and successes; otherwise, it will print without any color.
        output (TextIO | None, optional): An optional file-like object where the output should be written. Defaults to stdout if not provided.
        error (str, optional): The string to be used for indicating error messages. This will be colored red when `color` is True. Defaults to an empty string.
        success (str, optional): The string to be used for indicating successful operations. This will be colored green when `color` is True. Defaults to an empty string.
        
    Returns:
        BasicPrinter: An instance of the BasicPrinter or ColoramaPrinter class, depending on whether color output is enabled.
    """
    if color and not hasattr(colorama, "init"):  # Mocking colorama_unavailable for this example
        no_colorama_message = (
            "\n"
            "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
            "Reference: https://pypi.org/project/colorama/\n\n"
            "You can either install it separately on your system or as the colors extra "
            "for isort. Ex: \n\n"
            "$ pip install isort[colors]\n"
        )
        print(no_colorama_message, file=sys.stderr)
        sys.exit(1)

    if not hasattr(colorama, "init") or color:  # Mocking colorama_unavailable for this example
        colorama.init(strip=False)
    return (
        ColoramaPrinter(error, success, output) if color else BasicPrinter(error, success, output)
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_create_terminal_printer_0_test_invalid_inputs
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_invalid_inputs.py:6:25: E0602: Undefined variable 'TextIO' (undefined-variable)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_invalid_inputs.py:20:29: E0602: Undefined variable 'colorama' (undefined-variable)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_invalid_inputs.py:32:19: E0602: Undefined variable 'colorama' (undefined-variable)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_invalid_inputs.py:33:8: E0602: Undefined variable 'colorama' (undefined-variable)


"""