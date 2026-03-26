
import pytest
import re
from typing import Iterable, Generator, Tuple

def parse_env_file_contents(lines: Iterable[str] = None) -> Generator[Tuple[str, str], None, None]:
    for line in lines if lines is not None else []:
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
