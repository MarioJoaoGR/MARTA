
import pytest
from flutes.structure import no_map_instance

def test_none_input():
    with pytest.raises(TypeError):
        no_map_instance(None)
