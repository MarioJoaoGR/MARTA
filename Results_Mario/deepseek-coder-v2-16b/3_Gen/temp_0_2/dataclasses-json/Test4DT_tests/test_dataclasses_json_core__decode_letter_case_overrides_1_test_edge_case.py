
import pytest
from dataclasses_json import core

def test_edge_case():
    field_names = []
    overrides = {}
    
    result = core._decode_letter_case_overrides(field_names, overrides)
    
    assert result == {}, "Expected an empty dictionary for both empty field names and overrides"
