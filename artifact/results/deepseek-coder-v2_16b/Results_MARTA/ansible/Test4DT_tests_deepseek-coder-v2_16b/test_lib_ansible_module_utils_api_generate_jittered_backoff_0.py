
import pytest
from ansible.module_utils.api import generate_jittered_backoff
import random

def test_generate_jittered_backoff_default():
    jittered_backoff = list(generate_jittered_backoff())
    assert len(jittered_backoff) == 10, "Expected 10 delays but got {}".format(len(jittered_backoff))
    for delay in jittered_backoff:
        assert 0 <= delay <= 60, "Delay out of expected range (0-60): {}".format(delay)

def test_generate_jittered_backoff_custom():
    jittered_backoff = list(generate_jittered_backoff(retries=5, delay_base=2, delay_threshold=30))
    assert len(jittered_backoff) == 5, "Expected 5 delays but got {}".format(len(jittered_backoff))
    for delay in jittered_backoff:
        assert 0 <= delay <= 30, "Delay out of expected range (0-30): {}".format(delay)

def test_generate_jittered_backoff_minimum_retries():
    jittered_backoff = list(generate_jittered_backoff(retries=1))
    assert len(jittered_backoff) == 1, "Expected 1 delay but got {}".format(len(jittered_backoff))
    for delay in jittered_backoff:
        assert 0 <= delay <= 60, "Delay out of expected range (0-60): {}".format(delay)

def test_generate_jittered_backoff_maximum_delay_threshold():
    jittered_backoff = list(generate_jittered_backoff(delay_threshold=90))
    assert len(jittered_backoff) == 10, "Expected 10 delays but got {}".format(len(jittered_backoff))
    for delay in jittered_backoff:
        assert 0 <= delay <= 90, "Delay out of expected range (0-90): {}".format(delay)

def test_generate_jittered_backoff_custom_delay_base():
    jittered_backoff = list(generate_jittered_backoff(delay_base=4))
    assert len(jittered_backoff) == 10, "Expected 10 delays but got {}".format(len(jittered_backoff))
    for delay in jittered_backoff:
        assert 0 <= delay <= min(60, 4 * 2 ** (len(jittered_backoff)-1)), "Delay out of expected range (0-custom): {}".format(delay)
