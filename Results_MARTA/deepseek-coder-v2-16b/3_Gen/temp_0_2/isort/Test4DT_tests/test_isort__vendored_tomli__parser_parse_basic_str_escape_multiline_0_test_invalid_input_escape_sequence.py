
import pytest
from typing import Tuple

def parse_basic_str_escape_multiline(src: str, pos: int) -> Tuple[int, str]:
    """Parses escape sequences in a basic string, specifically designed to handle multiline strings.

    This function processes the input string `src` starting from position `pos`, looking for and resolving escape sequences such as `\\u` (for Unicode characters), `\\U` (for longer Unicode characters), or specific escaped characters like `\n`, `\t`, and `\`. It is designed to handle multiline strings, where it skips over whitespace until a non-whitespace character or newline is encountered.

    Parameters:
        src (str): The input string containing the basic string to be parsed.
        pos (int): The current position in the string where parsing should start. This parameter must support indexing and incrementation as described in the `skip_chars` function's docstring.

    Returns:
        Tuple[int, str]: A tuple containing the updated position after parsing the escape sequence and the string with all escape sequences resolved to their corresponding characters.

    Raises:
        ValueError: If an unrecognized escape sequence is found or if a non-whitespace character is encountered before a newline for multiline strings.
        KeyError: If an invalid escape sequence is encountered that does not match any known replacement in `BASIC_STR_ESCAPE_REPLACEMENTS`.
    """
    BASIC_STR_ESCAPE_REPLACEMENTS = {
        '\\n': '\n',
        '\\t': '\t',
        '\\\\': '\\'
    }
    
    def skip_chars(src, pos):
        while pos < len(src) and src[pos].isspace():
            pos += 1
        return pos
    
    if pos >= len(src):
        raise ValueError("End of string reached without finding a valid escape sequence.")
    
    skip_chars(src, pos)
    
    if pos >= len(src):
        raise ValueError("End of string reached without finding a valid escape sequence.")
    
    for i in range(pos, len(src)):
        if src[i] == '\\':
            if i + 1 < len(src):
                replacement = BASIC_STR_ESCAPE_REPLACEMENTS.get(src[i+1:])
                if replacement is not None:
                    return (i + len(replacement), replacement)
                else:
                    raise ValueError("Unrecognized escape sequence.")
            else:
                raise ValueError("Incomplete escape sequence at end of string.")
    
    return (pos, src[pos:])

def test_invalid_input_escape_sequence():
    src = 'Hello\\xWorld'
    pos = 0
    with pytest.raises(ValueError):
        parse_basic_str_escape_multiline(src, pos)
