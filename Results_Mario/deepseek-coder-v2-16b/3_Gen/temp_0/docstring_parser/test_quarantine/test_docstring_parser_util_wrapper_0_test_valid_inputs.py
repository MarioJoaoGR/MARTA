
from docstring_parser import parse, DocstringParam
from inspect import signature as Signature
from functools import wraps
from collections import ChainMap

# Assuming these are defined in the util module or imported correctly
def example_func1():
    '''Example function 1'''
    pass

def example_func2():
    '''Example function 2'''
    pass

def wrapper(func: _Func) -> _Func:
    """
    A function that wraps another function to combine its docstrings from multiple sources.
    
    This function takes a callable `func` and modifies its docstring by combining the documentation from itself and other functions provided in the `others` list (if any). The combined docstring includes parameters, short descriptions, long descriptions, and metadata from all involved functions.
    
    Parameters:
        func (_Func): The function whose docstring is to be modified. This should be a callable object that supports the `__doc__` attribute.
        
        others (list of callables): A list of additional functions whose docstrings are to be included in the combined docstring. Each function in this list should also support the `__doc__` attribute.
    
    Returns:
        _Func: The original function with its docstring modified to include information from all provided functions.
    
    Example:
        def example_func1():
            '''Example function 1'''
            pass
        
        def example_func2():
            '''Example function 2'''
            pass
        
        combined_doc = wrapper(example_func1)
        combined_doc.__doc__ = wrapper(combined_doc, example_func2)
        
        print(combined_doc.__doc__)
    
    Note:
        - The `others` parameter should be a list of callables that support the `__doc__` attribute. If no additional functions are provided, this parameter can be omitted or set to an empty list.
        - The function modifies the docstring of the original function by combining information from itself and all other functions in the `others` list.
    """
    @wraps(func)
    def inner_wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    sig = Signature.from_callable(func)
    comb_doc = parse(func.__doc__ or "")
    docs = [parse(other.__doc__ or "") for other in others] + [comb_doc]
    params = dict(
        ChainMap(
            *(
                {param.arg_name: param for param in doc.params}
                for doc in docs
            )
        )
    )

    for doc in reversed(docs):
        if not doc.short_description:
            continue
        comb_doc.short_description = doc.short_description
        comb_doc.blank_after_short_description = (
            doc.blank_after_short_description
        )
        break

    for doc in reversed(docs):
        if not doc.long_description:
            continue
        comb_doc.long_description = doc.long_description
        comb_doc.blank_after_long_description = (
            doc.blank_after_long_description
        )
        break

    combined = {}
    for doc in docs:
        metas = {}
        for meta in doc.meta:
            meta_type = type(meta)
            if meta_type in exclude:
                continue
            metas.setdefault(meta_type, []).append(meta)
        for meta_type, meta in metas.items():
            combined[meta_type] = meta

    combined[DocstringParam] = [
        params[name] for name in sig.parameters if name in params
    ]
    comb_doc.meta = list(chain(*combined.values()))
    func.__doc__ = compose(
        comb_doc, style=style, rendering_style=rendering_style
    )
    return func

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_util_wrapper_0_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:2:0: E0611: No name 'DocstringParam' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:16:18: E0602: Undefined variable '_Func' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:16:28: E0602: Undefined variable '_Func' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:52:10: E1101: Function 'signature' has no 'from_callable' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:54:52: E0602: Undefined variable 'others' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:87:28: E0602: Undefined variable 'exclude' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:96:25: E0602: Undefined variable 'chain' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:97:19: E0602: Undefined variable 'compose' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:98:24: E0602: Undefined variable 'style' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_valid_inputs.py:98:47: E0602: Undefined variable 'rendering_style' (undefined-variable)


"""