
import re
import pytest

def normalize_line(raw_line: str) -> tuple[str, str]:
    """Normalizes import related statements in the provided line.

    Returns (normalized_line: str, raw_line: str)
    """
    line = re.sub(r"from(\.+)cimport ", r"from \g<1> cimport ", raw_line)
    line = re.sub(r"from(\.+)import ", r"from \g<1> import ", line)
    line = line.replace("import*", "import *")
    line = re.sub(r" (\.+)import ", r" \g<1> import ", line)
    line = re.sub(r" (\.+)cimport ", r" \g<1> cimport ", line)
    line = line.replace("\t", " ")
    return line, raw_line

@pytest.mark.parametrize("raw_line", [None])
def test_edge_case_none(raw_line):
    with pytest.raises(TypeError):
        normalize_line(raw_line)
