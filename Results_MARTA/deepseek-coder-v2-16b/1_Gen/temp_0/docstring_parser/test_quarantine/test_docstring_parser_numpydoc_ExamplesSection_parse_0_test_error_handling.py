
import typing as T
from textwrap import dedent
from docstring_parser.numpydoc import DocstringExample, DocstringMeta

class ExamplesSection:
    """Parser for numpydoc examples sections.
    
    This class is designed to parse and extract `DocstringExample` objects from the body of a section that contains code snippets preceded by '>>>'. Each parsed object includes the key(s) associated with it, a snippet of code (if present), and a description (if provided). The function processes the input text by cleaning it and then splitting it into lines. It iterates through these lines to separate the code snippets from their descriptions, creating `DocstringExample` instances for each pair found.
    
    Args:
        text (str): The section body text that should be cleaned with ``inspect.cleandoc`` before parsing. This string represents the raw content of the documentation section where examples are provided.
        
    Yields:
        DocstringExample: An instance of `DocstringExample` containing the parsed metadata for each example found in the input text. The metadata includes keys, a code snippet (if available), and a description.
    
    Examples:
        >>> parser = ExamplesSection()
        >>> examples = list(parser.parse("""
        ... >>> import numpy as np
        ... >>> np.empty((2, 2))  # creates an empty matrix
        ... matrix([[0., 0.], [0., 0.]])
        ... """))
        >>> print(examples[0].keys)  # Outputs: ['import numpy as np']
        >>> print(examples[0].snippet)  # Outputs: np.empty((2, 2))
        >>> print(examples[0].description)  # Outputs: creates an empty matrix
    """
    
    def parse(self, text: str) -> T.Iterable[DocstringMeta]:
        """Parse ``DocstringExample`` objects from the body of this section.

        :param text: section body text. Should be cleaned with
                     ``inspect.cleandoc`` before parsing.
        """
        lines = dedent(text).strip().splitlines()
        while lines:
            snippet_lines = []
            description_lines = []
            while lines:
                if not lines[0].startswith(">>>"):
                    break
                snippet_lines.append(lines.pop(0))
            while lines:
                if lines[0].startswith(">>>"):
                    break
                description_lines.append(lines.pop(0))
            yield DocstringExample(
                [self.key],
                snippet="\n".join(snippet_lines) if snippet_lines else None,
                description="\n".join(description_lines),
            )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_error_handling
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_error_handling.py:20:8: E0001: Parsing failed: 'unexpected indent (Test4DT_tests.test_docstring_parser_numpydoc_ExamplesSection_parse_0_test_error_handling, line 20)' (syntax-error)

"""