
import pytest
from typesystem.fields import Field, Object

def test_object_init_with_properties():
    with pytest.raises(TypeError):
        name_field = Field('string')

def test_object_init_with_pattern_properties():
    with pytest.raises(TypeError):
        geo_field = Field('object')


def test_object_init_with_min_max_properties():
    with pytest.raises(TypeError):
        name_field = Field('string')