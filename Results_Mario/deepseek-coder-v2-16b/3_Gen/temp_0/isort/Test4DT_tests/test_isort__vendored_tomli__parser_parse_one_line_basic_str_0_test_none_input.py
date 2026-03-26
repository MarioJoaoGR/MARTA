
from typing import Tuple

import pytest

from isort._vendored.tomli._parser import Pos, parse_one_line_basic_str


def test_none_input():
    with pytest.raises(TypeError):
        parse_one_line_basic_str(None, Pos(0))
