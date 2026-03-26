
import pytest
from dataclasses_json.core import _ExtendedEncoder
from datetime import datetime
from decimal import Decimal
from uuid import UUID
from enum import Enum
import json

def test_valid_collection_sequence():
    encoder = _ExtendedEncoder()
    sequence_obj = [1, 2, 3]
    
    # Test if the default method correctly handles a list (sequence)
    assert encoder.default(sequence_obj) == [1, 2, 3]
