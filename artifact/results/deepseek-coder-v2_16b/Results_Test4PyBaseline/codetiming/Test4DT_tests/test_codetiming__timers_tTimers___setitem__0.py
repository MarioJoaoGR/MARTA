
import pytest
from codetiming import Timer
import time
import logging

# Test Case 1: Creating and Starting a Timer
def test_timer_creation_and_start():
    timer = Timer(name="fetch_data")
    assert hasattr(timer, '_start_time'), "Timer should have a start time attribute"