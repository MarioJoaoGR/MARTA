
import re
import inspect
from typing import Optional, List, Tuple, Dict, Any
from docstring_parser.epydoc import (
    Docstring,
    DocstringStyle,
    DocstringParam,
    DocstringReturns,
    DocstringRaises,
    ParseError,
)

def parse(text: Optional[str]) -> Docstring:
    """Parse the epydoc-style docstring into its components.

    :returns: parsed docstring
    """
    ret = Docstring(style=DocstringStyle.EPYDOC)
    if not text:
        return ret

    text = inspect.cleandoc(text)
    match = re.search("^@", text, flags=re.M)
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

    param_pattern = re.compile(r"(param|keyword|type)(\s+[_A-z][_A-z0-9]*\??):")
    attribute_pattern = re.compile(r"(ivar|cvar|var)(\s+[_A-z][_A-z0-9]*\??):")
    raise_pattern = re.compile(r"(raise)(\s+[_A-z][_A-z0-9]*\??)?:")
    return_pattern = re.compile(r"(return|rtype|yield|ytype):")
    meta_pattern = re.compile(r"([_A-z][_A-z0-9]+)((\s+[_A-z][_A-z0-9]*\??)*):")

    # tokenize
    stream: List[Tuple[str, str, List[str], str]] = []
    for match in re.finditer(r"^@.*?(?=^@|\Z)", meta_chunk, flags=re.S | re.M):
        chunk = match.group(0)
        if not chunk:
            continue

        param_match = re.search(param_pattern, chunk)
        attribute_match = re.search(attribute_pattern, chunk)
        raise_match = re.search(raise_pattern, chunk)
        return_match = re.search(return_pattern, chunk)
        meta_match = re.search(meta_pattern, chunk)

        match = param_match or attribute_match or raise_match or return_match or meta_match
        if not match:
            raise ParseError(f'Error parsing meta information near "{chunk}".')

        desc_chunk = chunk[match.end() :]
        if "\n" in desc_chunk:
            first_line, rest = desc_chunk.split("\n", 1)
            desc_chunk = first_line + "\n" + inspect.cleandoc(rest)
        stream.append((param_match and "param" or attribute_match and "attribute" or "return", match.group(1), [match.group(2).strip()], desc_chunk.strip()))

    # Combine type_name, arg_name, and description information
    params: Dict[str, Dict[str, Any]] = {}
    for base, key, args, desc in stream:
        if base not in ["param", "attribute", "return"]:
            continue  # nothing to do

        (arg_name,) = args or ("return",)
        info = params.setdefault(arg_name, {})
        info_key = "type_name" if "type" in key else "description"
        info[info_key] = desc

        if base == "return":
            is_generator = key in {"ytype", "yield"}
            if info.setdefault("is_generator", is_generator) != is_generator:
                raise ParseError(f'Error parsing meta information for "{arg_name}".')

    is_done: Dict[str, bool] = {}
    for base, key, args, desc in stream:
        if base in ["param", "attribute"] and not is_done.get(args[0], False):
            (arg_name,) = args
            info = params[arg_name]
            type_name = info.get("type_name")

            if type_name and type_name.endswith("?"):
                is_optional = True
                type_name = type_name[:-1]
            else:
                is_optional = False

            match = re.match(r".*defaults to (.+)", desc, flags=re.DOTALL)
            default = match.group(1).rstrip(".") if match else None

            meta_item = DocstringParam(
                args=[key, arg_name],
                description=info.get("description"),
                arg_name=arg_name,
                type_name=type_name,
                is_optional=is_optional,
                default=default,
            )
            is_done[arg_name] = True
        elif base == "return" and not is_done.get("return", False):
            info = params["return"]
            meta_item = DocstringReturns(
                args=[key],
                description=info.get("description"),
                type_name=info.get("type_name"),
                is_generator=info.get("is_generator", False),
            )
            is_done["return"] = True
        elif base == "raise":
            (type_name,) = args or (None,)
            meta_item = DocstringRaises(
                args=[key] + args,
                description=desc,
                type_name=type_name,
            )
        elif base == "meta":
            meta_item = DocstringMeta(
                args=[key] + args,
                description=desc,
            )
        else:
            (key, *_) = args or ("return",)
            assert is_done.get(key, False)
            continue  # don't append

        ret.meta.append(meta_item)

    return ret

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_epydoc_parse_0_test_empty_input
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_parse_0_test_empty_input.py:127:24: E0602: Undefined variable 'DocstringMeta' (undefined-variable)

"""