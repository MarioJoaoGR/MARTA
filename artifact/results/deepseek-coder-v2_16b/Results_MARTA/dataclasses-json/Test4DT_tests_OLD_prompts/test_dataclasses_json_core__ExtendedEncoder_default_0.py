
import pytest
from datetime import datetime, timedelta
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json
from dataclasses_json.core import _ExtendedEncoder

class MyEnum(Enum):
    VALUE = "enum_value"


def test_invalid_inputs():
    encoder = _ExtendedEncoder()

    # Unsupported type (lambda function)
    unsupported_input = lambda x: x
    with pytest.raises(TypeError):
        encoder.default(unsupported_input)