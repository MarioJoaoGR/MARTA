
import pytest
from flutes.structure import no_map_instance

def test_edge_case_none():
    invalid_input = None
    with pytest.raises(TypeError):
        no_map_instance(invalid_input)
