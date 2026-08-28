
import pytest
from datetime import time
from typesystem.formats import TimeFormat

# Test serialization of a valid time object
def test_valid_time_serialization():
    tf = TimeFormat()
    valid_time = time(12, 30, 45)
    result = tf.serialize(valid_time)
    assert result == '12:30:45'

# Test serialization of None input
def test_none_input_serialization():
    tf = TimeFormat()
    none_input = None
    result = tf.serialize(none_input)
    assert result is None

# Test serialization of an invalid type (string)
def test_invalid_type_serialization():
    tf = TimeFormat()
    invalid_obj = 'invalid'
    with pytest.raises(AssertionError):
        tf.serialize(invalid_obj)
