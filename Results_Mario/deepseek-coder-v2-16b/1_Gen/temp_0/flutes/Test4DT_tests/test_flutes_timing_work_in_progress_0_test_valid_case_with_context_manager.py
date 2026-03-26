
import pytest
from flutes.timing import work_in_progress
import time

@pytest.fixture(autouse=True)
def mock_time():
    original_time = time.time

    def mock_sleep(*args, **kwargs):
        return 0

    time.time = mock_sleep
    yield
    time.time = original_time

def test_valid_case_with_context_manager():
    with work_in_progress("Test task"):
        time.sleep(1)
