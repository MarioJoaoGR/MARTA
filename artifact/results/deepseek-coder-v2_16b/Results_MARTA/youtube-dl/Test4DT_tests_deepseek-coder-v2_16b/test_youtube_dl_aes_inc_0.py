
import pytest
from youtube_dl.aes import inc


def test_inc_wraparound():
    assert inc([255, 255, 255]) == [0, 0, 0]
