
import pytest
from datetime import time
from typesystem.formats import TimeFormat

# Scenario 1: Test serialization of a valid time object
def test_valid_time_serialization():
    tf = TimeFormat()
    valid_time = time(12, 30, 45)
    serialized_time = tf.serialize(valid_time)
    assert serialized_time == '12:30:45', f"Expected ISO formatted time string for a valid time object, but got {serialized_time}"

# Scenario 2: Test serialization of an invalid type should raise AssertionError