
import pytest
from thonny.roughparse import StringTranslatePseudoMapping


def test_edge_case():
    non_defaults = {}
    mapping = StringTranslatePseudoMapping(non_defaults, lambda x: ord('*'))
    
    text = "ab"
    with pytest.raises(TypeError):
        translated_text = text.translate(mapping)
