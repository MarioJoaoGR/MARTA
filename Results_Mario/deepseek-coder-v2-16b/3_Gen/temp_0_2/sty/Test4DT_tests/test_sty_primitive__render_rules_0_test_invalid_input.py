
import pytest
from sty.primitive import _render_rules, RenderType, Style, StylingRule, Renderfuncs

def test_invalid_input():
    renderfuncs = {}
    rules = [123]  # Invalid input type
    
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, rules)
