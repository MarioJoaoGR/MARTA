
import pytest
import re
from typing import Iterable, Generator, Tuple

def parse_env_file_contents(lines: Iterable[str] = None) -> Generator[Tuple[str, str], None, None]:
    """
    Parses the contents of an environment file.

    This function takes an iterable of strings representing lines from an env file and yields key-value pairs parsed from those lines. It handles single quotes, double quotes, and escapes within the values.

    Parameters:
        lines (Iterable[str]): An iterable containing the lines from the env file. If None, it will be treated as an empty list.

    Yields:
        Tuple[str, str]: A tuple where the first element is the key and the second element is the parsed value. The value is stripped of surrounding quotes and escape sequences are handled.

    Examples:
        >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
        >>> list(parse_env_file_contents(lines))
        [('TEST', '.../yeee'), ('THISIS', '.../a/test'), ('YOLO', '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')]
    """
    if lines is None:
        return
    for line in lines:
        m1 = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
        if m1:
            key, val = m1.group(1), m1.group(2)
            m2 = re.match(r"\A'(.*)'\Z", val)
            if m2:
                val = m2.group(1)
            m3 = re.match(r'\A"(.*)"\Z', val)
            if m3:
                val = re.sub(r'\\(.)', r'\1', m3.group(1))
            yield key, val

@pytest.mark.parametrize("lines", [None])
def test_none_input(lines):
    result = list(parse_env_file_contents(lines))
    assert len(result) == 0
