
import pytest
from pymonet.monad_try import Try

class Validation:
    """It that can hold either a success value or a failure value and has methods for accumulating errors."""
    
    def __init__(self, value, errors):
        self.value = value
        self.errors = errors

    def add_error(self, error):
        """Appends a new error message to the `errors` list.
        
        Parameters:
            error (str): The error message to be added to the list of accumulated errors.
        """
        self.errors.append(error)

    def apply_function(self, mapper):
        """Take function (A) -> B and applied this function on current Validation value.
        
        Parameters:
            mapper (Callable[[A], B]): A function that takes a value of type A and returns a value of type B.
            
        Returns:
            A new instance of `Validation` with the mapped value and previous errors. If there are any accumulated errors, it returns None and prints all stored error messages.
        """
        if self.errors:
            print(self.errors)
            return None
        else:
            return Validation(mapper(self.value), self.errors)

    def is_success(self):
        return len(self.errors) == 0

    def to_try(self):
        """
        Transform Validation to Try.

        :returns: successfully Try with Validation value value. Try is successful when Validation has no errors
        :rtype: Try[A]
        """
        from pymonet.monad_try import Try

        return Try(self.value, is_success=self.is_success())

def test_edge_case_none():
    val = Validation(None, ['Error'])
    result = val.apply_function(lambda x: x * 2)
    assert result is None
    assert val.errors == ['Error']
