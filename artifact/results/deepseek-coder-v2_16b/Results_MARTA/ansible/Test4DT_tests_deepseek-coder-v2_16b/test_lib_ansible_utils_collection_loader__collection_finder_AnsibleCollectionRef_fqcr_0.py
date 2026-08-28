
import pytest
from ansible.utils.collection_loader._collection_finder import AnsibleCollectionRef


def test_edge_case():
    with pytest.raises(ValueError) as e:
        acr = AnsibleCollectionRef(None, None, None, None)
    assert str(e.value) == "invalid collection name (must be of the form namespace.collection): None"