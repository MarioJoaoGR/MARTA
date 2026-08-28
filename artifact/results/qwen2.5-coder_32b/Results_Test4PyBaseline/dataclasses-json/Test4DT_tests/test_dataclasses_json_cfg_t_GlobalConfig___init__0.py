# Module: dataclasses_json.cfg
import pytest
from dataclasses_json.cfg import _GlobalConfig
from typing import Callable
import datetime
from marshmallow import fields

def test_global_config_initialization():
    config = _GlobalConfig()
    assert isinstance(config.encoders, dict)
    assert isinstance(config.decoders, dict)
    assert isinstance(config.mm_fields, dict)

def test_registering_encoders():
    config = _GlobalConfig()
    config.encoders[int] = lambda x: str(x)
    config.encoders[datetime.date] = lambda x: x.isoformat()

    assert config.encoders[int](123) == '123'
    assert config.encoders[datetime.date](datetime.date(2023, 9, 15)) == '2023-09-15'

def test_registering_decoders():
    config = _GlobalConfig()
    config.decoders[str] = lambda x: int(x)
    config.decoders[datetime.date] = lambda x: datetime.datetime.fromisoformat(x).date()

    assert config.decoders[str]('123') == 123
    assert config.decoders[datetime.date]('2023-09-15') == datetime.date(2023, 9, 15)

def test_registering_marshmallow_fields():
    config = _GlobalConfig()
    config.mm_fields[datetime.date] = fields.Date()

    example_date = datetime.date(2023, 9, 15)
    encoded_date = config.mm_fields[datetime.date]._serialize(example_date, None, None)
    decoded_date = config.mm_fields[datetime.date]._deserialize(encoded_date, None, None)

    assert encoded_date == '2023-09-15'
    assert decoded_date == example_date

def test_missing_encoder():
    config = _GlobalConfig()
    with pytest.raises(KeyError):
        config.encoders[int](123)  # No encoder registered for int

def test_missing_decoder():
    config = _GlobalConfig()
    with pytest.raises(KeyError):
        config.decoders[str]('123')  # No decoder registered for str

def test_missing_marshmallow_field():
    config = _GlobalConfig()
    example_date = datetime.date(2023, 9, 15)
    with pytest.raises(KeyError):
        config.mm_fields[datetime.date]._serialize(example_date, None, None)  # No Marshmallow field registered for date
