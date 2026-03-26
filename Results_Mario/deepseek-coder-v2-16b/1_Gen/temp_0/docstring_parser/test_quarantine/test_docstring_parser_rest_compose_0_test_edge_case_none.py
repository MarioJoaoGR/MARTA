
import pytest
from docstring_parser import Docstring, RenderingStyle
from dataclasses import dataclass
from typing import List, Optional as T

@dataclass
class DocstringParam:
    arg_name: str = ""
    type_name: str = ""
    is_optional: bool = False
    description: str = ""

@dataclass
class DocstringReturns:
    type_name: str = ""
    is_generator: bool = False
    description: str = ""

@dataclass
class DocstringRaises:
    type_name: str = ""
    description: str = ""

def compose(
    docstring: Docstring,
    rendering_style: RenderingStyle = RenderingStyle.COMPACT,
    indent: str = "    ",
) -> str:
    """Render a parsed docstring into formatted docstring text.

    This function takes a parsed `docstring` object and renders it into a string with specific formatting based on the provided `rendering_style`. The style can be one of 'compact', 'clean', or 'expanded'. Additionally, an optional `indent` parameter allows customization of the whitespace used for indentation.

    Parameters:
        docstring (Docstring): A parsed representation of the docstring to be rendered.
        rendering_style (RenderingStyle, optional): The style in which to render the docstring. Defaults to 'compact'. Must be one of 'compact', 'clean', or 'expanded'.
        indent (str, optional): The string used for indentation. Defaults to "    ".

    Returns:
        str: A formatted string representation of the provided `docstring`.

    Examples:
        >>> from dataclasses import dataclass
        >>> @dataclass
        ... class Docstring:
        ...     short_description: str = ""
        ...     long_description: str = ""
        ...     meta: List[Any] = field(default_factory=list)
        ... 
        >>> doc = Docstring(short_description="A function", long_description="Long description")
        >>> print(compose(doc))
        A function
        
        >>> print(compose(doc, rendering_style=RenderingStyle.CLEAN))
        A function
        
        >>> print(compose(doc, indent="  "))
        A function

    Note:
        The `rendering_style` parameter determines the layout of the output string. 'compact' will place all parts closely together without additional whitespace or indentation. 'clean' and 'expanded' add more structure by separating descriptions with newlines and adding appropriate indentation for parameters, returns, and raises sections.
    """
    def process_desc(desc: T.Optional[str]) -> str:
        if not desc:
            return ""

        if rendering_style == RenderingStyle.CLEAN:
            (first, *rest) = desc.splitlines()
            return "\n".join([" " + first] + [indent + line for line in rest])

        if rendering_style == RenderingStyle.EXPANDED:
            (first, *rest) = desc.splitlines()
            return "\n".join(
                ["\n" + indent + first] + [indent + line for line in rest]
            )

        return " " + desc

    parts: T.List[str] = []
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
            if meta.type_name:
                type_text = (
                    f" {meta.type_name}? "
                    if meta.is_optional
                    else f" {meta.type_name} "
                )
            else:
                type_text = " "
            if rendering_style == RenderingStyle.EXPANDED:
                text = f":param {meta.arg_name}:"
                text += process_desc(meta.description)
                parts.append(text)
                if type_text[:-1]:
                    parts.append(f":type {meta.arg_name}:{type_text[:-1]}")
            else:
                text = f":param{type_text}{meta.arg_name}:"
                text += process_desc(meta.description)
                parts.append(text)
        elif isinstance(meta, DocstringReturns):
            type_text = f" {meta.type_name}" if meta.type_name else ""
            key = "yields" if meta.is_generator else "returns"

            if rendering_style == RenderingStyle.EXPANDED:
                if meta.description:
                    text = f":{key}:"
                    text += process_desc(meta.description)
                    parts.append(text)
                if type_text:
                    parts.append(f":rtype:{type_text}")
            else:
                text = f":{key}{type_text}:"
                text += process_desc(meta.description)
                parts.append(text)
        elif isinstance(meta, DocstringRaises):
            type_text = f" {meta.type_name} " if meta.type_name else ""
            text = f":raises{type_text}:" + process_desc(meta.description)
            parts.append(text)
        else:
            text = f':{" ".join(meta.args)}:' + process_desc(meta.description)
            parts.append(text)
    return "\n".join(parts)

# Test case for edge case where docstring is None
def test_edge_case_none():
    with pytest.raises(TypeError):
        compose(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest_compose_0_test_edge_case_none
docstring_parser/Test4DT_tests/test_docstring_parser_rest_compose_0_test_edge_case_none.py:3:0: E0611: No name 'Docstring' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_rest_compose_0_test_edge_case_none.py:3:0: E0611: No name 'RenderingStyle' in module 'docstring_parser' (no-name-in-module)

"""