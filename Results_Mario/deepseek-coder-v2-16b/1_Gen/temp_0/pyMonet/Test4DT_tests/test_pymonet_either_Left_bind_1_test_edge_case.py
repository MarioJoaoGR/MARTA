
from pymonet.either import Left, Right

def test_edge_case():
    left_instance = Left(None)  # Create an instance of Left with a value
    result = left_instance.bind(lambda x: x + 1)  # The lambda function is not used because it's a Left instance
    assert isinstance(result, Left)  # Check that the result is still a Left instance
    assert result.value is None  # Check that the stored value remains unchanged
