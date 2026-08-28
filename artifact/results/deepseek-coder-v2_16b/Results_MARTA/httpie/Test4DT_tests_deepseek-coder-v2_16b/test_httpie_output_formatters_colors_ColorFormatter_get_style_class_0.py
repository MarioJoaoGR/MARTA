
import pytest
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment
import sys
import io




def test_get_style_class():
    from pygments.styles import get_all_styles
    style_classes = list(get_all_styles())
    for style in style_classes:
        assert hasattr(ColorFormatter, 'get_style_class'), "ColorFormatter should have a method get_style_class"
        assert callable(ColorFormatter.get_style_class), "get_style_class should be a callable function"
        assert isinstance(ColorFormatter.get_style_class(style), type), f"Expected {style} to return a style class, but got a different type"