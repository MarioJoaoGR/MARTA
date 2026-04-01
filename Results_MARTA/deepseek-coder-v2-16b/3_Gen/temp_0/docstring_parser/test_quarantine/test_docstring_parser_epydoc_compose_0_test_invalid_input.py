
import pytest
from docstring_parser import parse, Docstring, RenderingStyle
from typing import List, Union
from dataclasses import dataclass, field

@dataclass
class ExampleDocstring:
    short_description: str = "A short description"
    long_description: str = "This is a longer description."
    meta: List[Union[DocstringParam, DocstringReturns, DocstringRaises]] = field(default_factory=list)

@dataclass
class DocstringParam:
    arg_name: str
    type_name: str
    is_optional: bool
    description: str

@dataclass
class DocstringReturns:
    type_name: str
    is_generator: bool
    description: str

@dataclass
class DocstringRaises:
    type_name: str
    description: str

def compose(
    docstring: Docstring,
    rendering_style: RenderingStyle = RenderingStyle.COMPACT,
    indent: str = "    ",
) -> str:
    """Render a parsed docstring into formatted docstring text.

    This function takes a parsed `docstring` object and renders it into a string with specific formatting based on the provided `rendering_style`. The style can be either compact or expanded, affecting how detailed information is presented. Additionally, an optional `indent` parameter allows customization of the whitespace used for indentation.

    Parameters:
        docstring (Docstring): A parsed representation of the docstring to be rendered.
        rendering_style (RenderingStyle): The style in which the docstring should be rendered. Default is RenderingStyle.COMPACT.
            - RenderingStyle.COMPACT: Renders a compact version with minimal whitespace and indentation, suitable for concise displays.
            - RenderingStyle.EXPANDED: Renders an expanded version with more detailed information, including additional lines for parameters and return types.
        indent (str): The string to use as the indentation character(s). Default is "    " (four spaces).

    Returns:
        str: A formatted string representing the rendered docstring.

    Examples:
        >>> from dataclasses import dataclass
        >>> @dataclass
        ... class ExampleDocstring:
        ...     short_description: str = "A short description"
        ...     long_description: str = "This is a longer description."
        ...     meta: List[Union[DocstringParam, DocstringReturns, DocstringRaises]] = field(default_factory=list)
        >>> example_docstring = ExampleDocstring()
        >>> print(compose(example_docstring))
        A short description
        
        This is a longer description.

    Notes:
        - The function processes different types of metadata (parameters, returns, raises) and formats them according to the specified rendering style.
        - If `rendering_style` is set to RenderingStyle.EXPANDED or (RenderingStyle.CLEAN and not is_type), detailed descriptions are indented properly.
        - For optional parameters, a question mark (`?`) is appended to indicate their optionality in the type specification.
    """
    def process_desc(desc: str, is_type: bool) -> str:
        if not desc:
            return ""

        if rendering_style == RenderingStyle.EXPANDED or (
            rendering_style == RenderingStyle.CLEAN and not is_type
        ):
            lines = desc.splitlines()
            indented_lines = [indent + line for line in lines]
            return "\n".join([""] + indented_lines)

        lines = desc.splitlines()
        indented_lines = [indent + line for line in lines]
        return " ".join(lines[0:1]) + " " + " ".join(indented_lines[1:])

    parts = []
    if docstring.short_description:
        parts.append(docstring.short_description)
    if docstring.blank_after_short_description:
        parts.append("")
    if docstring.long_description:
        parts.append(docstring.long_description)
    if docstring.blank_after_long_description:
        parts.append("")

    for meta in docstring.meta:
        if isinstance(meta, DocstringParam):
            type_name = f"{meta.type_name}?" if meta.is_optional else meta.type_name
            text = f"@type {meta.arg_name}:" + process_desc(type_name, True)
            parts.append(text)
        elif isinstance(meta, DocstringReturns):
            type_key = "yield" if meta.is_generator else "return"
            text = f"@{type_key}:" + process_desc(meta.type_name, True)
            parts.append(text)
        elif isinstance(meta, DocstringRaises):
            text = f"@raise {meta.type_name}:" if meta.type_name else "@raise:"
            parts.append(text + process_desc(meta.description, False))
        else:
            text = f'@{" ".join(meta.args)}:' + process_desc(meta.description, False)
            parts.append(text)
    return "\n".join(parts)

def test_invalid_input():
    with pytest.raises(TypeError):
        compose("invalid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_epydoc_compose_0_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_compose_0_test_invalid_input.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_compose_0_test_invalid_input.py:3:0: E0611: No name 'Docstring' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_compose_0_test_invalid_input.py:3:0: E0611: No name 'RenderingStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_compose_0_test_invalid_input.py:11:21: E0601: Using variable 'DocstringParam' before assignment (used-before-assignment)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_compose_0_test_invalid_input.py:11:37: E0601: Using variable 'DocstringReturns' before assignment (used-before-assignment)
docstring_parser/Test4DT_tests/test_docstring_parser_epydoc_compose_0_test_invalid_input.py:11:55: E0601: Using variable 'DocstringRaises' before assignment (used-before-assignment)


"""