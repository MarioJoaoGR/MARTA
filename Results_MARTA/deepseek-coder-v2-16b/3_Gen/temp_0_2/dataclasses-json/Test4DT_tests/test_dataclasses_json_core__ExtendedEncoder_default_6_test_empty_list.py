
import pytest
from dataclasses_json.core import _ExtendedEncoder, Json
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json

def test_empty_list():
    encoder = _ExtendedEncoder()
    empty_list = []
    assert encoder.default(empty_list) == []
