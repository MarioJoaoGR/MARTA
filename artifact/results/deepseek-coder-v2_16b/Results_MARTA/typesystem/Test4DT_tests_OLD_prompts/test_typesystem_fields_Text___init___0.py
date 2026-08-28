
import pytest
from typesystem.fields import Text, Field



def test_invalid_inputs():
    with pytest.raises(TypeError):
        text_obj_invalid = Text(invalid_attr='invalid_value')