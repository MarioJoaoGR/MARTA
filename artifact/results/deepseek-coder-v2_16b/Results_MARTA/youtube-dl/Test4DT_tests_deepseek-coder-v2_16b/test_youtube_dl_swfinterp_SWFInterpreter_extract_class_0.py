
import pytest
from youtube_dl.swfinterp import SWFInterpreter
from youtube_dl.utils import ExtractorError
import io


def test_invalid_input():
    with pytest.raises(ExtractorError):
        swf_content = b'\x00\x01\x02'  # Not a valid SWF file header
        interpreter = SWFInterpreter(swf_content)


