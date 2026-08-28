
import pytest
from mimesis.providers.cryptographic import Cryptographic
from uuid import UUID

def test_uuid_default():
    crypto = Cryptographic()
    uuid_str = crypto.uuid()
    assert isinstance(UUID(uuid_str), UUID)

def test_uuid_as_object():
    crypto = Cryptographic()
    uuid_obj = crypto.uuid(as_object=True)
    assert isinstance(uuid_obj, UUID)

@pytest.mark.parametrize("locale", ["xyz"])
def test_invalid_locale(locale):
    with pytest.raises(TypeError):
        Cryptographic(locale=locale)
