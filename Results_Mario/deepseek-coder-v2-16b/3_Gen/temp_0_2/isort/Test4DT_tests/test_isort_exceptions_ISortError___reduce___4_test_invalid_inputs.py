
from isort.exceptions import ISortError

def test_invalid_inputs():
    try:
        raise ISortError("An error occurred in isort")
    except ISortError as e:
        assert str(e) == "An error occurred in isort"
