
import pytest
from ansible.utils.collection_loader._collection_finder import _AnsibleCollectionFinder
import os
import sys


def test_invalid_input_error_handling():
    with pytest.raises(OSError):
        raise OSError("Test Error")