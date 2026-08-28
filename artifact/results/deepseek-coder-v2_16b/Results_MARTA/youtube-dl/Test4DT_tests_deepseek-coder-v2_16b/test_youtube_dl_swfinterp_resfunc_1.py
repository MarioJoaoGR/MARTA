
import pytest
from youtube_dl.swfinterp import SWFInterpreter, ExtractorError


def test_edge_case():
    with pytest.raises(TypeError):
        swf = SWFInterpreter()

def test_invalid_input():
    with pytest.raises(ExtractorError):
        swf = SWFInterpreter(file_contents="dummy file contents")