
import pytest


def parse_hex_char(src: str, pos: int, hex_len: int) -> tuple[int, str]:
    """Parses a hexadecimal character from the given source string at the specified position with the defined length.

    This function extracts a substring of `hex_len` characters starting from the `pos` index in the `src` string. It then checks if this substring consists only of valid hexadecimal digits and has the exact length of `hex_len`. If not, it raises an error indicating that the hex value is invalid. After validating the hex value, it converts it to an integer and checks whether it represents a valid Unicode scalar value. If the conversion results in a character that cannot be represented as a Unicode scalar value, it also raises an error.

    Parameters:
        src (str): The input string from which the hexadecimal character is to be parsed. This should be the complete content of the file or data structure being parsed.
        pos (int): The position within the `src` string where the parsing starts. This is typically an index indicating the character offset from the start of the string.
        hex_len (int): The length of the hexadecimal substring to be extracted and validated.

    Returns:
        Tuple[int, str]: A tuple containing the updated position in the source string after parsing the hex value and the parsed hexadecimal character as a string.

    Raises:
        ValueError: If the extracted substring does not consist only of valid hexadecimal digits or if its length is not equal to `hex_len`.
        UnicodeError: If the converted integer from the hex string does not represent a valid Unicode scalar value.
    """
    hex_str = src[pos : pos + hex_len]
    if len(hex_str) != hex_len or not all(c in '0123456789abcdefABCDEF' for c in hex_str):
        raise ValueError("Invalid hex value")
    pos += hex_len
    hex_int = int(hex_str, 16)
    if not (0 <= hex_int <= 0x10FFFF and (hex_int <= 0xD7FF or hex_int >= 0xE000) and (not (0x10FFFF < hex_int <= 0x10FFFF))):
        raise UnicodeError("Escaped character is not a Unicode scalar value")
    return pos, chr(hex_int)

def test_valid_input():
    src = '48656c6c6f20776f726c6421'
    pos = 0
    hex_len = 2
    expected_pos = 2
    expected_char = 'H'
    
    result_pos, result_char = parse_hex_char(src, pos, hex_len)
    
    assert result_pos == expected_pos
    assert result_char == expected_char
