
import pytest
from typesystem.fields import Field, NO_DEFAULT


def test_field_union():
    with pytest.raises(TypeError):
        Field(str)