
import pytest
import random
from ansible.module_utils.api import generate_jittered_backoff

# Test the function with default parameters
def test_generate_jittered_backoff_default():
    random.seed(0)  # Seed for reproducibility
    delays = list(generate_jittered_backoff())
    assert len(delays) == 10, "Expected 10 delays but got {}".format(len(delays))
    for delay in delays:
        assert 0 <= delay <= 60, "Delay {} is out of the expected range (0-60)".format(delay)

# Test the function with specified number of retries and base delay
def test_generate_jittered_backoff_specified():
    random.seed(0)  # Seed for reproducibility
    delays = list(generate_jittered_backoff(retries=5, delay_base=2))
    assert len(delays) == 5, "Expected 5 delays but got {}".format(len(delays))
    expected_max = min(60, 2 ** 5 * 2)  # Calculate the maximum possible delay with specified parameters
    for delay in delays:
        assert 0 <= delay <= expected_max, "Delay {} is out of the expected range (0-{})".format(delay, expected_max)

# Test the function with a specific number of retries, base delay, and lower delay threshold
def test_generate_jittered_backoff_specific():
    random.seed(0)  # Seed for reproducibility
    delays = list(generate_jittered_backoff(retries=8, delay_base=1, delay_threshold=15))
    assert len(delays) == 8, "Expected 8 delays but got {}".format(len(delays))
    for delay in delays:
        assert 0 <= delay <= 15, "Delay {} is out of the expected range (0-15)".format(delay)

# Test the function with a large number of retries to ensure it handles larger values correctly
def test_generate_jittered_backoff_large_retries():
    random.seed(0)  # Seed for reproducibility
    delays = list(generate_jittered_backoff(retries=20, delay_base=1))
    assert len(delays) == 20, "Expected 20 delays but got {}".format(len(delays))
    expected_max = min(60, 1 * 2 ** 20)  # Calculate the maximum possible delay with specified parameters
    for delay in delays:
        assert 0 <= delay <= expected_max, "Delay {} is out of the expected range (0-{})".format(delay, expected_max)

# Test to cover line 130 and 131 directly
def test_generate_jittered_backoff_coverage():
    random.seed(0)  # Seed for reproducibility
    retries = 5
    delay_base = 2
    delays = list(generate_jittered_backoff(retries=retries, delay_base=delay_base))
    
    assert len(delays) == retries, f"Expected {retries} delays but got {len(delays)}"
    
    for retry in range(retries):
        expected_max = min(60, delay_base * 2 ** retry)
        actual_delay = delays[retry]
        assert 0 <= actual_delay <= expected_max, f"Delay for retry {retry} is out of the expected range (0-{expected_max})"
