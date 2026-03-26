
import pytest
from decimal import Decimal
from dataclasses_json.core import _ExtendedEncoder

def test_valid_decimal():
    encoder = _ExtendedEncoder()
    dec_obj = Decimal('123.45')
    assert encoder.default(dec_obj) == '123.45'
