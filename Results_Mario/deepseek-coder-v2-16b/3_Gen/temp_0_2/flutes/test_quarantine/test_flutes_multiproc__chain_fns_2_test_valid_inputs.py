
from typing import List, Callable, Tuple, Any, Dict

def _chain_fns(fns: List[Callable[..., R]], fn_arg_kwargs: List[Tuple[Tuple[Any, ...], Dict[str, Any]]]) -> List[R]:
    """
    Executes a list of functions with provided arguments and keyword arguments.
    
    This function takes two lists as input: `fns`, which is a list of callable functions, 
    and `fn_arg_kwargs`, which is a list of tuples where each tuple contains a tuple of positional 
    arguments (args) and a dictionary of keyword arguments (kwargs). The function applies each 
    function in `fns` to its corresponding arguments and keyword arguments from `fn_arg_kwargs`.
    
    Parameters:
        fns (List[Callable[..., R]]): A list of callable functions. Each function should take a variable number of arguments (`*args`) and can accept keyword arguments (`**kwargs`).
        fn_arg_kwargs (List[Tuple[Tuple[Any, ...], Dict[str, Any]]]): A list of tuples where each tuple contains:
            - A tuple of positional arguments (args) that will be passed to the corresponding function in `fns`.
            - A dictionary of keyword arguments (kwargs) that will also be passed to the corresponding function.
    
    Returns:
        List[R]: A list containing the results of applying each function in `fns` with its respective arguments and keyword arguments from `fn_arg_kwargs`.
    
    Example:
        Suppose we have two functions, `func1` and `func2`, and their corresponding argument-keyword pairs:
        
        ```python
        def func1(a, b):
            return a + b
        
        def func2(x, y=0):
            return x * y
        
        fns = [func1, func2]
        fn_arg_kwargs = [( (1, 2), {} ), ( (3,), {'y': 4} )]
        
        result = _chain_fns(fns, fn_arg_kwargs)
        ```
        
        In this example:
        - `func1` is called with arguments `(1, 2)` and no keyword arguments.
        - `func2` is called with arguments `(3,)` and the keyword argument `y=4`.
        The result will be a list containing the results of these function calls: `[3, 12]`.
    
    Notes:
        Ensure that the length of `fns` matches the length of `fn_arg_kwargs`, as each function in `fns` must have its corresponding arguments and keyword arguments provided.
    """
    rets = []
    for fn, (args, kwargs) in zip(fns, fn_arg_kwargs):
        rets.append(fn(*args, **kwargs))
    return rets

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc__chain_fns_2_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_valid_inputs.py:4:39: E0602: Undefined variable 'R' (undefined-variable)
flutes/Test4DT_tests/test_flutes_multiproc__chain_fns_2_test_valid_inputs.py:4:113: E0602: Undefined variable 'R' (undefined-variable)


"""