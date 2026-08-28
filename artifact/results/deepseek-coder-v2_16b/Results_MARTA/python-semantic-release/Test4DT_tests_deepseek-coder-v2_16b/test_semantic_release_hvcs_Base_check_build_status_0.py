
import pytest
from semantic_release.hvcs import Base

class Subclass(Base):
    def check_build_status(self, owner: str, repo: str, ref: str) -> bool:
        raise NotImplementedError

def test_valid_input():
    subclass_instance = Subclass()
    with pytest.raises(NotImplementedError):
        subclass_instance.check_build_status('owner', 'repo', 'ref')

def test_edge_case():
    subclass_instance = Subclass()
    with pytest.raises(NotImplementedError):
        subclass_instance.check_build_status('owner', 'repo', 'ref')
