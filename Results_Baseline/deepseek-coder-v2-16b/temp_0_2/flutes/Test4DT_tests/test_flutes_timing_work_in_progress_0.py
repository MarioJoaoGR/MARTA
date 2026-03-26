
# Module: flutes.timing
import pytest
from flutes.timing import work_in_progress
import sys
import io
import pickle

# Test the function with a default description
def test_work_in_progress_default():
    @work_in_progress()
    def dummy_function():
        pass
    # Capture the output to verify the message and timing
    captured_output = []
    stdout_original = sys.stdout
    try:
        import io
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        dummy_function()
        sys.stdout = stdout_original
        captured_output.append(new_stdout.getvalue())
    except Exception as e:
        sys.stdout = stdout_original
        raise e
    
    assert "Work in progress... done." in captured_output[0]

# Test the function with a custom description
def test_work_in_progress_custom():
    @work_in_progress("Custom Description")
    def dummy_function():
        pass
    # Capture the output to verify the message and timing
    captured_output = []
    stdout_original = sys.stdout
    try:
        import io
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        dummy_function()
        sys.stdout = stdout_original
        captured_output.append(new_stdout.getvalue())
    except Exception as e:
        sys.stdout = stdout_original
        raise e
    
    assert "Custom Description... done." in captured_output[0]

# Test the function using a context manager with a custom description
def test_work_in_progress_context_manager():
    path = "/tmp/dummyfile"  # Assuming this is a valid file path for testing
    obj = b'test data'  # Example object to be saved and loaded
    captured_output = []
    stdout_original = sys.stdout
    try:
        import io
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        with work_in_progress("Context Manager Test"):
            with open(path, "wb") as f:
                pickle.dump(obj, f)
        sys.stdout = stdout_original
        captured_output.append(new_stdout.getvalue())
    except Exception as e:
        sys.stdout = stdout_original
        raise e
    
    assert "Context Manager Test... done." in captured_output[0]
