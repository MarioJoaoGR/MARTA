
import pytest
from inspect import getfullargspec
from typing import Callable, Sequence, Dict, Any, List, Tuple

class ArgReplacer:
    def __init__(self, func: Callable, name: str) -> None:
        self.name = name
        try:
            self.arg_pos = getfullargspec(func).args.index(name)  # type: Optional[int]
        except ValueError:
            # Not a positional parameter
            self.arg_pos = None

    def _getargnames(self, func: Callable) -> List[str]:
        try:
            return getfullargspec(func).args
        except TypeError:
            if hasattr(func, "func_code"):
                code = func.func_code  # type: ignore
                return code.co_varnames[: code.co_argcount]
            raise

    def get_old_value(self, args: Sequence[Any], kwargs: Dict[str, Any], default: Any = None) -> Any:
        if self.arg_pos is not None and len(args) > self.arg_pos:
            return args[self.arg_pos]
        else:
            return kwargs.get(self.name, default)

    def replace(self, new_value: Any, args: Sequence[Any], kwargs: Dict[str, Any]) -> Tuple[Any, Sequence[Any], Dict[str, Any]]:
        if self.arg_pos is not None and len(args) > self.arg_pos:
            old_value = args[self.arg_pos]
            args = list(args)  # *args is normally a tuple
            args[self.arg_pos] = new_value
        else:
            old_value = kwargs.get(self.name)
            kwargs[self.name] = new_value
        return old_value, args, kwargs

# Example function
def example_function(a, b=2):
    pass

# Instantiate ArgReplacer with the target function and argument name
arg_replacer = ArgReplacer(example_function, 'b')

# Test initialization
def test_init():
    assert arg_replacer.name == 'b'
    assert isinstance(arg_replacer.arg_pos, int)

# Test get_old_value method
def test_get_old_value():
    args = ()  # No positional arguments provided
    kwargs = {'b': 10}  # Provide a new value for 'b' in kwargs
    old_value = arg_replacer.get_old_value(args, kwargs)