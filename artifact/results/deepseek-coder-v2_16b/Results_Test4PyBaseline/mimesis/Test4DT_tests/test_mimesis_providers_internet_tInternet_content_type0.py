
# Module: mimesis.providers.internet
# test_internet.py
from mimesis.providers.internet import Internet
from mimesis.enums import MimeType, FileType
import pytest

@pytest.fixture
def internet():
    return Internet()

def test_content_type_default(internet):
    content_type = internet.content_type()
    assert isinstance(content_type, str)