
import pytest
from mimesis import Internet
from mimesis.enums import MimeType

@pytest.fixture(scope="module")
def internet_instance():
    return Internet(seed=42)

def test_Internet_content_type_basic(internet_instance):
    content_type = internet_instance.content_type()
    assert isinstance(content_type, str), "Expected a string representation of the content type"
    assert content_type.startswith("Content-Type:"), "Expected the content type to start with 'Content-Type:'"
