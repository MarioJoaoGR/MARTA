
import time
import pytest
from flutes.timing import work_in_progress

def test_valid_input_decorator():
    def dummy_function():
        time.sleep(0.1)

    # Since the decorator does not raise an exception, we need to check if it prints correctly
    from io import StringIO
    import sys

    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    @work_in_progress("Testing decorator")
    def decorated_function():
        dummy_function()

    decorated_function()

    sys.stdout = old_stdout
    output = new_stdout.getvalue().strip()
    assert "Testing decorator... done." in output
    assert "(0.10s)" in output or "(0.11s)" in output

def test_valid_input_context_manager():
    from io import StringIO
    import sys

    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    with work_in_progress("Testing context manager"):
        time.sleep(0.1)

    sys.stdout = old_stdout
    output = new_stdout.getvalue().strip()
    assert "Testing context manager... done." in output
    assert "(0.10s)" in output or "(0.11s)" in output



def test_invalid_input_none_description_context_manager():
    with pytest.raises(TypeError):
        with work_in_progress(None):
            pass

def test_invalid_input_non_string_description_context_manager():
    with pytest.raises(TypeError):
        with work_in_progress(123):
            pass