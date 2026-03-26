# Module: pymonet.maybe
# test_maybe.py
import pytest
from pymonet.monad_try import Try
from pymonet.maybe import Maybe

# Test creating a Maybe with a value and converting it to Try
def test_maybe_with_value():
    maybe = Maybe(value=42, is_nothing=False)  # Creates a Maybe with the value 42.
    try_instance = maybe.to_try()
    assert try_instance.is_success == True
    assert try_instance.value == 42

# Test creating a Maybe that represents nothing and converting it to Try
def test_maybe_with_nothing():
    maybe_none = Maybe(None, is_nothing=True)  # Creates a Maybe that represents no value.
    try_instance_none = maybe_none.to_try()
    assert try_instance_none.is_success == False
    assert try_instance_none.value is None

# Test using to_try in a function that handles Try instances
def test_process_maybe():
    def process_maybe(maybe):
        try_instance = maybe.to_try()
        if try_instance.is_success:
            print("The contained value is:", try_instance.value)
        else:
            print("The Maybe object contains no value.")

    # Example usage with a Maybe that has a value
    process_maybe(Maybe(value=42, is_nothing=False))  # Outputs: The contained value is: 42

    # Example usage with a Maybe that represents nothing
    process_maybe(Maybe(None, is_nothing=True))       # Outputs: The Maybe object contains no value.

# Run the tests
if __name__ == "__main__":
    pytest.main()
