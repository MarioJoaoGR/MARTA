
import pytest
from dataclasses_json.core import _ExtendedEncoder, Json
import json
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum

def test_none_input():
    encoder = _ExtendedEncoder()
    none_obj = None
    
    with pytest.raises(TypeError):
        encoder.default(none_obj)
