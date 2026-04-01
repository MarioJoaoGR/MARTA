
import pytest
from unittest.mock import patch
from dataclasses_json.mm import SchemaF

def test_invalid_inputs():
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()
