
import pytest
from dataclasses_json.core import _ExtendedEncoder, Json
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum
import json

def test_valid_collection_mapping():
    encoder = _ExtendedEncoder()
    mapping_obj = {'key': 'value'}
    
    # Test if the encoder correctly handles a valid collection (mapping) object
    assert encoder.default(mapping_obj) == {'key': 'value'}
