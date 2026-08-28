
import pytest
from unittest.mock import patch
from semantic_release.hvcs import Base
from typing import Optional

class Subclass(Base):
    def token(self) -> Optional[str]:
        raise NotImplementedError

def test_subclass_token():
    subclass = Subclass()
    with pytest.raises(NotImplementedError):
        subclass.token()
