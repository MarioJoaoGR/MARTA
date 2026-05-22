
from httpie.output.ui.palette import BOLD, ITALIC

class ColorString:
    """A class representing a string with specific color and style attributes.

    This class allows for combining different styles and properties to create colored strings. The `__or__` method is used to combine the current instance's styles with additional styles or properties provided as arguments.

    Parameters:
        other (str, GenericColor, _StyledGenericColor): An object representing a style or property to be combined with the current ColorString instance.

    Returns:
        ColorString: A new ColorString instance that includes the combined styles and properties.

    Examples:
        >>> from httpie.output.ui.palette import BOLD, ITALIC
        >>> cs = ColorString(PieColor.BLUE)
        >>> styled_cs = cs | BOLD | ITALIC
        >>> print(styled_cs)  # Output will be a blue string with bold and italic styles
    """
    def __or__(self, other: str) -> 'ColorString':
        """Combine a style with a property.

        E.g: PieColor.BLUE | BOLD | ITALIC
        """
        if isinstance(other, str):
            # In case of PieColor.BLUE | SOMETHING
            # we just create a new string.
            return ColorString(self + ' ' + other)
        elif isinstance(other, GenericColor):
            # If we see a GenericColor, then we'll wrap it
            # in with the desired property in a different class.
            return _StyledGenericColor(other, styles=self.split())
        elif isinstance(other, _StyledGenericColor):
            # And if it is already wrapped, we'll just extend the
            # list of properties.
            other.styles.extend(self.split())
            return other
        else:
            return NotImplemented

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:2:0: E0611: No name 'BOLD' in module 'httpie.output.ui.palette' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:2:0: E0611: No name 'ITALIC' in module 'httpie.output.ui.palette' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:30:31: E0602: Undefined variable 'GenericColor' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:33:19: E0602: Undefined variable '_StyledGenericColor' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:33:53: E1101: Instance of 'ColorString' has no 'split' member (no-member)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:34:31: E0602: Undefined variable '_StyledGenericColor' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_ui_palette_ColorString___or___0_test_valid_input_basic_usage.py:37:32: E1101: Instance of 'ColorString' has no 'split' member (no-member)


"""