
import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE


def test_none_input():
    extractor = LinuxAcademyIE()
    with pytest.raises(TypeError):
        extractor._real_initialize(None)
