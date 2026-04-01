
import pytest
from sty.primitive import _render_rules, RenderType, Style, StylingRule, Renderfuncs

def test_invalid_input():
    renderfuncs = {}
    rules = "string"  # Invalid type: should raise ValueError
    
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, rules)
