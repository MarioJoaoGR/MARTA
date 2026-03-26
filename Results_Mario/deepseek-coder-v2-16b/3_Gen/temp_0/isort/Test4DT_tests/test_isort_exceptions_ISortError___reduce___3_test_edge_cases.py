
from isort.exceptions import ISortError


class CustomISortError(ISortError):
    """Custom isort exception for specific errors."""
    pass

def test_edge_cases():
    try:
        raise CustomISortError("An error occurred in the edge case scenario.")
    except CustomISortError as e:
        assert str(e) == "An error occurred in the edge case scenario."
