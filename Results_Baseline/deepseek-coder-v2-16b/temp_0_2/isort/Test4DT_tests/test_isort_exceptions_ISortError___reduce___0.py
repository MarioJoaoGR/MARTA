
# Module: isort.exceptions
# test_isort_exceptions.py
import pytest

from isort.exceptions import (ExistingSyntaxErrors, IntroducedSyntaxErrors,
                              ISortError)


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
    assert str(exc_info.value) == "A custom error occurred in isort processing."

def test_introduced_syntax_errors():
    with pytest.raises(IntroducedSyntaxErrors) as exc_info:
        raise IntroducedSyntaxErrors("example/file/path.py")