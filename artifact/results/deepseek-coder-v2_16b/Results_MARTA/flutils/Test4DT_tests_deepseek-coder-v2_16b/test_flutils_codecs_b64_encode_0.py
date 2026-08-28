
import pytest
from flutils.codecs.b64 import encode
import base64


def test_invalid_base64_input():
    text = 'InvalidBase64String'
    with pytest.raises(UnicodeEncodeError):
        encode(text)

