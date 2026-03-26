
import pytest
from itertools import accumulate
from operator import add
from functools import reduce
from typing import Callable, Iterable, Iterator, Any

def scanl(func: Callable[[Any, Any], Any], iterable: Iterable[Any]) -> Iterator[Any]:
    """
    Applies a binary function cumulatively to the elements of an iterable.
    
    The `scanl` function takes two arguments:
    
    - `func`: A callable that takes two arguments (the result from the previous application and the next element in the iterable) and returns a new value. This is the binary function that will be applied cumulatively to the elements of the iterable.
    - `iterable`: An iterable object, such as a list or generator, whose elements will be processed by the cumulative function.
    
    The function applies `func` cumulatively to the items of `iterable`, from left to right, so as to reduce the iterable to a single value. It returns an iterator that yields the intermediate results after each application of `func`.
    
    Examples:
    
    ```python
    # Example usage with addition function
    def add(x, y):
        return x + y
    
    result = list(scanl(add, [1, 2, 3, 4]))
    print(result)  # Output: [1, 3, 6, 10]
    
    # Example usage with multiplication function
    def multiply(x, y):
        return x * y
    
    result = list(scanl(multiply, [1, 2, 3, 4]))
    print(result)  # Output: [1, 2, 6, 24]
    ```
    
    In the first example, `add` is a function that adds two numbers. The scanl function applies this function cumulatively to the list of numbers, yielding intermediate sums as it progresses. In the second example, `multiply` multiplies two numbers. Applying this function cumulatively to the list results in an iterator that yields products after each step.
    
    Note: This function is similar to Python's built-in `itertools.accumulate`, but specifically tailored for a left-to-right cumulative application of a binary function, as found in functional programming languages like Haskell.
    ```
    """
    it = iter(iterable)
    try:
        yield next(it)  # First element is the initial value
    except StopIteration:
        return  # If iterable is empty, just return immediately
    
    accumulator = next(it)  # Start with the second element
    for item in it:
        accumulator = func(accumulator, item)
        yield accumulator

# Test invalid input raising TypeError
def test_invalid_input():
    with pytest.raises(TypeError):
        list(scanl(add, [1, "2", 3, 4]))
