
import pytest
from flutes.timing import work_in_progress

def test_valid_case_context_manager():
    with work_in_progress("Saving file"):
        # Simulate some code that would normally be timed
        pass
