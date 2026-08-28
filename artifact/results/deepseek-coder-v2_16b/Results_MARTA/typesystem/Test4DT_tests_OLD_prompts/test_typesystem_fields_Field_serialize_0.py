
import pytest
from typesystem.fields import Field, NO_DEFAULT

def test_invalid_inputs():
    with pytest.raises(AssertionError):
        Field(title=123, description="The name of the person", default="John Doe", allow_null=False)
    
    with pytest.raises(AssertionError):
        Field(title="Name", description=123, default="John Doe", allow_null=False)


def test_no_default_value_with_allow_null():
    field = Field(title="Name", description="The name of the person", allow_null=True)
    assert field.allow_null == True
    assert field.default is None