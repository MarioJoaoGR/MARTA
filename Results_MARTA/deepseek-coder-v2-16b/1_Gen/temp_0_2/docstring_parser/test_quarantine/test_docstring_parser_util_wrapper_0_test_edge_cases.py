
from docstring_parser import parse, DocstringParam
from inspect import Signature
from collections import ChainMap
from itertools import chain

def wrapper(func: _Func) -> _Func:
    """
    A function that wraps another function to enhance its docstring with combined and formatted metadata from multiple sources.

    Parameters:
        func (_Func): The function to be wrapped. It should accept a single argument which is the function being wrapped.

    Returns:
        _Func: The original function with an enhanced docstring that includes combined and formatted metadata from all provided sources.

    Example:
        To use this wrapper, you can define multiple functions each with their own docstrings and then combine them using the wrapper. For example:
        
        def func1():
            '''Function 1 description'''
            pass
        
        def func2():
            '''Function 2 description'''
            pass
        
        combined_func = wrapper(func1)
        combined_func.__doc__ += '\n' + wrapper(func2).__doc__
        
        This example demonstrates how to combine the docstrings of two functions into a single, enhanced docstring.
    """
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
************* Module Test4DT_tests.test_docstring_parser_util_wrapper_0_test_edge_cases
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:2:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:2:0: E0611: No name 'DocstringParam' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:7:18: E0602: Undefined variable '_Func' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:7:28: E0602: Undefined variable '_Func' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:36:52: E0602: Undefined variable 'others' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:69:28: E0602: Undefined variable 'exclude' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:79:19: E0602: Undefined variable 'compose' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:80:24: E0602: Undefined variable 'style' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_wrapper_0_test_edge_cases.py:80:47: E0602: Undefined variable 'rendering_style' (undefined-variable)


"""