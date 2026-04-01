
import pytest
from docstring_parser.common import DocstringStyle

class Docstring:
    """Docstring object representation."""
    
    def __init__(self, style=None):  # type: ignore
        """Initialize self."""
        if style is not None and not isinstance(style, DocstringStyle):
            raise ValueError("Invalid style argument. It should be an instance of DocstringStyle.")
        
        self.short_description = None  # type: ignore
        self.long_description = None  # type: ignore
        self.blank_after_short_description = False
        self.blank_after_long_description = False
        self.meta = []  # type: ignore
        self.style = style  # type: ignore

    def description(self) -> str | None:
        """Return the full description of the function"""
        ret = []
        if self.short_description:
            ret.append(self.short_description)
            if self.blank_after_short_description:
                ret.append("")
        if self.long_description:
            ret.append(self.long_description)

        if not ret:
            return None

        return "\n".join(ret)

def test_error_case():
    with pytest.raises(ValueError):
        Docstring(style="invalid_style")
