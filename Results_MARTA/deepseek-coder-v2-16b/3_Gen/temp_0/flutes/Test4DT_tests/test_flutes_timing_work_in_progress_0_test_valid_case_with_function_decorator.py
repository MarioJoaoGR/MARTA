
import pytest
from flutes.timing import work_in_progress
import time

@pytest.fixture(autouse=True)
def mock_time():
    original_time = time.time
    times = [0]  # Use a list to make it mutable

    def mocked_time():
        return times[0] if len(times) == 1 else original_time()

    time.time = mocked_time
    yield
    time.time = original_time

def test_valid_case_with_function_decorator():
    @work_in_progress("Test task")
    def dummy_function():
        pass

    # Capture the output of print statements
    import sys
    from io import StringIO
    captured_output = StringIO()
    sys.stdout = captured_output

    dummy_function()

    sys.stdout = sys.__stdout__
    assert "Test task... done." in captured_output.getvalue()
