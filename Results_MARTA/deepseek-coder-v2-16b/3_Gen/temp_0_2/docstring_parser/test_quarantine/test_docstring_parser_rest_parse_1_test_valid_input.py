
import re
import inspect
from typing import Optional, List
from docstring_parser.rest import Docstring, DocstringStyle, ParseError, DocstringParam, DocstringReturns

def parse(text: Optional[str]) -> Docstring:
    """Parse the ReST-style docstring into its components.

    The `parse` function takes a string `text` that represents a ReStructuredText (ReST) style docstring and parses it into a structured format, including short descriptions, long descriptions, metadata for parameters, return values, etc. It supports parsing of various meta-information directives such as :param, :type, :return, etc., which are common in Python docstrings written in this style.

    Parameters:
        text (Optional[str]): The input string containing the ReST-style docstring to be parsed. This parameter is optional and can be None if no documentation is provided.
            - If `text` is provided, it should be a string that starts with meta-information directives like :param or :return.
            - Changes to this parameter may affect how detailed information such as types, descriptions for parameters, and return values are parsed from the docstring.

    Returns:
        Docstring: A `Docstring` object containing the parsed metadata including short descriptions, long descriptions, and detailed meta-information about each parameter and return value.
    """
    ret = Docstring(style=DocstringStyle.REST)
    if not text:
        return ret

    text = inspect.cleandoc(text)
    match = re.search("^:", text, flags=re.M)
    if match:
        desc_chunk = text[: match.start()]
        meta_chunk = text[match.start() :]
    else:
        desc_chunk = text
        meta_chunk = ""

    parts = desc_chunk.split("\n", 1)
    ret.short_description = parts[0] or None
    if len(parts) > 1:
        long_desc_chunk = parts[1] or ""
        ret.blank_after_short_description = long_desc_chunk.startswith("\n")
        ret.blank_after_long_description = long_desc_chunk.endswith("\n\n")
        ret.long_description = long_desc_chunk.strip() or None

    types = {}
    rtypes = {}
    for match in re.finditer(
        r"(^:.*?)(?=^:|\Z)", meta_chunk, flags=re.S | re.M
    ):
        chunk = match.group(0)
        if not chunk:
            continue
        try:
            args_chunk, desc_chunk = chunk.lstrip(":").split(":", 1)
        except ValueError as ex:
            raise ParseError(
                f'Error parsing meta information near "{chunk}".'
            ) from ex
        args = args_chunk.split()
        desc = desc_chunk.strip()

        if "\n" in desc:
            first_line, rest = desc.split("\n", 1)
            desc = first_line + "\n" + inspect.cleandoc(rest)

        # Add special handling for :type a: typename
        if len(args) == 2 and args[0] == "type":
            types[args[1]] = desc
        elif len(args) in [1, 2] and args[0] == "rtype":
            rtypes[None if len(args) == 1 else args[1]] = desc
        else:
            ret.meta.append(_build_meta(args, desc))

    for meta in ret.meta:
        if isinstance(meta, DocstringParam):
            meta.type_name = meta.type_name or types.get(meta.arg_name)
        elif isinstance(meta, DocstringReturns):
            meta.type_name = meta.type_name or rtypes.get(meta.return_name)

    if not any(isinstance(m, DocstringReturns) for m in ret.meta) and rtypes:
        for return_name, type_name in rtypes.items():
            ret.meta.append(
                DocstringReturns(
                    args=[],
                    type_name=type_name,
                    description=None,
                    is_generator=False,
                    return_name=return_name,
                )
            )

    return ret

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest_parse_1_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_rest_parse_1_test_valid_input.py:68:28: E0602: Undefined variable '_build_meta' (undefined-variable)


"""