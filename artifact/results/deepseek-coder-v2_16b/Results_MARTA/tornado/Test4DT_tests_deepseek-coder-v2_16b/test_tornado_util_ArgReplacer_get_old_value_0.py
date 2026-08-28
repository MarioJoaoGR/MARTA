
import pytest
from typing import Callable, Sequence, Dict, Any

class ArgReplacer:
    """
    Replaces one value in an ``args, kwargs`` pair.
    
    This class inspects the function signature to find an argument by name whether it is passed by position or keyword. It is designed for use in decorators and similar wrappers.
    
    Parameters:
        func (Callable): The Python callable object (function, method, etc.) whose arguments are to be inspected.
        name (str): The name of the argument to replace.
        
    Attributes:
        name (str): The name of the argument to replace.
        arg_pos (Optional[int]): The position of the argument in the function's signature if found, otherwise None.
    
    Examples:
        >>> def example_func(a, b=10):
        ...     return a + b
        ... 
        >>> replacer = ArgReplacer(example_func, 'b')
        >>> result = example_func(5)
        >>> print(result)  # Output: 15 (since default value of b is overridden by the replacement)
        
    How to use it:
        1. Import the necessary module or class.
        2. Create an instance of ArgReplacer with a callable and the name of the argument you want to replace.
        3. Use the replacer as needed in your decorators or wrappers.
    
    Note:
        The function assumes that the provided callable is either a Python function, method, or similar callable object. If the callable does not have a recognizable signature (e.g., if it's dynamically generated), this implementation may fail to find the argument by name and will raise an appropriate error.
    
    Initializes an instance of `ArgReplacer` with a specific function and argument to replace.
    
    Parameters:
        func (Callable): The Python callable object (function, method, etc.) whose arguments are to be inspected.
        name (str): The name of the argument to replace.
    """
    def __init__(self, func: Callable, name: str) -> None:
        self.name = name
        try:
            self.arg_pos = self._getargnames(func).index(name)  # type: Optional[int]
        except ValueError:
            # Not a positional parameter
            self.arg_pos = None

    def get_old_value(
        self, args: Sequence[Any], kwargs: Dict[str, Any], default: Any = None
    ) -> Any:
        """Returns the old value of the named argument without replacing it.

        Returns ``default`` if the argument is not present.
        """
        if self.arg_pos is not None and len(args) > self.arg_pos:
            return args[self.arg_pos]
        else:
            return kwargs.get(self.name, default)

    def _getargnames(self, func: Callable) -> Sequence[str]:
        """Helper method to get the argument names of a function."""
        import inspect
        sig = inspect.signature(func)
        return tuple(sig.parameters.keys())

# Test cases for ArgReplacer class



def test_missing_argument():
    def func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(func, 'b')
    old_value = replacer.get_old_value(args=(5,), kwargs={})
    assert old_value is None

def test_get_old_value():
    def func(a, b=10):
        return a + b
    
    replacer = ArgReplacer(func, 'b')
    old_value = replacer.get_old_value(args=(5,), kwargs={'b': 10})
    assert old_value == 10