
# Importing the ISortError from the correct module
from isort.exceptions import ISortError

def test_error_handling():
    try:
        raise ISortError("An error occurred in isort")
    except ISortError as e:
        assert str(e) == "An error occurred in isort"
