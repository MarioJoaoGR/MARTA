
# Module: isort.exceptions
# test_isort_exceptions.py
from functools import partial

import pytest

from isort.exceptions import ISortError, UnsupportedSettings


def test_basic_usage():
    with pytest.raises(ISortError) as exc_info:
        raise ISortError("An error occurred in isort processing.")
    assert str(exc_info.value) == "An error occurred in isort processing."

def test_custom_isort_error():
    class CustomISortError(ISortError):
        """Custom isort exception for specific errors."""
        pass
    
    with pytest.raises(CustomISortError) as exc_info:
        raise CustomISortError("A custom error occurred in isort processing.")