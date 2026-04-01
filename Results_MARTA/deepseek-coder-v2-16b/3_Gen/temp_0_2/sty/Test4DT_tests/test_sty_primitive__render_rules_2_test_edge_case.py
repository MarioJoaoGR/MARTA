
import pytest
from sty.primitive import _render_rules, RenderType, Style, StylingRule, Renderfuncs

def test_edge_case():
    renderfuncs = {}
    rules = [None, [], {}, ()]
    
    with pytest.raises(ValueError):
        _render_rules(renderfuncs, rules)
