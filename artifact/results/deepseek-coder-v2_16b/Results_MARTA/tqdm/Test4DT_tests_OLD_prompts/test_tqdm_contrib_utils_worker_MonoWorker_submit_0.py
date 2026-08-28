
import pytest
from tqdm.contrib.utils_worker import MonoWorker
from concurrent.futures import ThreadPoolExecutor, Future
from collections import deque
from unittest.mock import patch

@pytest.fixture
def mono_worker():
    return MonoWorker()

# Test scenario: Submitting a task and checking if it's not done immediately
def test_valid_input(mono_worker):
    def task1():
        print("Task 1 is running")
    
    # Submit the first task
    future1 = mono_worker.submit(task1)
    assert not future1.done(), "The first task should not have completed yet"

# Test scenario: Submitting multiple tasks and checking if the most recent one is executed

# Test scenario: Submitting a task and checking if it's done after execution

# Test scenario: Submitting a lambda function and checking if it's not called