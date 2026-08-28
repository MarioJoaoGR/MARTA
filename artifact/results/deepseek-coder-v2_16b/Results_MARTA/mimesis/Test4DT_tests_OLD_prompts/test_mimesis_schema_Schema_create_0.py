
import pytest
from mimesis.schema import Schema, UndefinedSchema
from unittest.mock import patch



def test_invalid_schema():
    with pytest.raises(UndefinedSchema):
        Schema("not_a_callable")