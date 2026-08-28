
import pytest
from youtube_dl.jsinterp import JSInterpreter


def test_edge_cases():
    with pytest.raises(TypeError):
        interpreter = JSInterpreter()
