
from semantic_release.hvcs import Base
import pytest
from typing import Optional

class Subclass(Base):
    def token(self) -> Optional[str]:
        raise NotImplementedError

def test_subclass_token():
    subclass = Subclass()
    with pytest.raises(NotImplementedError):
        assert subclass.token() is None
