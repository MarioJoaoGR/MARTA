
from inspect import signature
from functools import wraps
from docstring_parser import parse, DocstringStyle, RenderingStyle
from typing import Callable, Iterable, Type, ChainMap
from itertools import chain

# Assuming the following imports are available in your module
# from docstring_parser.util import combine_docstrings, _Func, DocstringMeta

def combine_docstrings(*others: Callable, exclude: Iterable[Type[DocstringMeta]] = (), style: DocstringStyle = DocstringStyle.AUTO, rendering_style: RenderingStyle = RenderingStyle.COMPACT) -> Callable:
    """A function decorator that parses the docstrings from `others`, programmatically combines them with the parsed docstring of the decorated function, and replaces the docstring of the decorated function with the composed result. Only parameters that are part of the decorated function's signature are included in the combined docstring. When multiple sources for a parameter or docstring metadata exist, the decorator will default to the wrapped function's value (when available) and otherwise use the rightmost definition from ``others``.

    Parameters:
        *others (_Func): The callables (functions, methods, etc.) from which to parse docstrings.
        exclude (Iterable[Type[DocstringMeta]]): An iterable of ``DocstringMeta`` subclasses to exclude when combining docstrings.
        style (DocstringStyle): The style for the composed docstring. The default will infer the style from the decorated function.
        rendering_style (RenderingStyle): The rendering style used to compose a docstring.

    Returns:
        _Func: The decorated function with a modified docstring.
    """
    def wrapper(func: Callable) -> Callable:
        sig = signature(func)
        comb_doc = parse(func.__doc__ or "")
        docs = [parse(other.__doc__ or "") for other in others] + [comb_doc]
        params = dict(ChainMap(*({param.arg_name: param for param in doc.params} for doc in docs)))

        for doc in reversed(docs):
            if not doc.short_description:
                continue
            comb_doc.short_description = doc.short_description
            comb_doc.blank_after_short_description = doc.blank_after_short_description
            break

        for doc in reversed(docs):
            if not doc.long_description:
                continue
            comb_doc.long_description = doc.long_description
            comb_doc.blank_after_long_description = doc.blank_after_long_description
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

        combined[DocstringParam] = [params[name] for name in sig.parameters if name in params]
        comb_doc.meta = list(chain(*combined.values()))
        func.__doc__ = compose(comb_doc, style=style, rendering_style=rendering_style)
        
        return func
    return wrapper

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_util_combine_docstrings_0_test_valid_inputs
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:4:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:4:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:4:0: E0611: No name 'RenderingStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:11:65: E0602: Undefined variable 'DocstringMeta' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:54:17: E0602: Undefined variable 'DocstringParam' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_util_combine_docstrings_0_test_valid_inputs.py:56:23: E0602: Undefined variable 'compose' (undefined-variable)


"""