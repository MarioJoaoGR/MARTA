
import pytest
from typing import List, Union

def decode_raw_args(
    args: List[Union[str, bytes]],
    stdin_encoding: str
) -> List[str]:
    """
    Convert all byte arguments to strings by decoding them using the specified encoding.

    Parameters:
        args (List[Union[str, bytes]]): A list containing either string or byte objects that need to be decoded.
        stdin_encoding (str): The encoding to use when decoding byte objects to strings.

    Returns:
        List[str]: A list of strings where each element is the result of decoding the corresponding argument from `args`. If an argument is already a string, it remains unchanged.

    Examples:
        >>> decode_raw_args(['hello', b'world'], 'utf-8')
        ['hello', 'world']
        
        >>> decode_raw_args([b'\xe4\xb8\xad\xe6\x96\x87', '中文'], 'utf-8')
        ['hello', 'world']
        
        >>> decode_raw_args(['hello', b'world'], 'ascii')
        Traceback (most recent call last):
            ...
        UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)
        
    Notes:
        - The function assumes that the provided encoding is supported and valid.
        - If an argument is a bytes object, it will be decoded using the specified encoding.
        - If an argument is already a str (string), it remains unchanged.
        - This function raises a `UnicodeDecodeError` if the specified encoding cannot decode a byte string.
    """
    return [
        arg.decode(stdin_encoding)
        if type(arg) is bytes else arg
        for arg in args
    ]

def test_none_input():
    with pytest.raises(TypeError):
        decode_raw_args(None, 'utf-8')
