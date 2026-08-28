
import pytest
from unittest.mock import patch
from mimesis.schema import Schema, UndefinedSchema


def test_invalid_schema_noncallable():
    with pytest.raises(UndefinedSchema):
        Schema("not_a_callable")