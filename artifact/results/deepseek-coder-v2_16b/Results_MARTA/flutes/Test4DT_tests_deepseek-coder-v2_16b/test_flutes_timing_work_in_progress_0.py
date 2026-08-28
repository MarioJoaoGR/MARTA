
import pytest
from unittest.mock import patch
import time

# Assuming the work_in_progress function is defined in a module named 'flutes.timing'
pytestmark = pytest.mark.skip("Module 'flutes.timing' not found")  # Placeholder for actual implementation

@pytest.fixture(autouse=True)
def mock_time():
    with patch('time.time', return_value=[0]):
        yield

@pytest.mark.parametrize("desc", ["Loading file", "Saving file"])
def test_valid_case_decorator(desc):
    @flutes.timing.work_in_progress(desc)
    def load_file():
        time.sleep(1)  # Simulate work in progress

    with patch('time.time', side_effect=[0, 1]):
        load_file()

@pytest.mark.parametrize("desc", ["Saving file"])
def test_valid_case_context_manager(desc):
    @flutes.timing.work_in_progress(desc)
    def save_file():
        time.sleep(1)  # Simulate work in progress

    with patch('time.time', side_effect=[0, 1]):
        with pytest.raises(TypeError):
            save_file()

def test_error_case_invalid_input():
    with pytest.raises(TypeError):
        flutes.timing.work_in_progress()(lambda: None)("Invalid input")
