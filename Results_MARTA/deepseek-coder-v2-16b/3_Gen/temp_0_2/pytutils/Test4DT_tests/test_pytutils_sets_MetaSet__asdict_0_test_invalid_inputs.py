
import pytest
from pytutils.sets import MetaSet
import attr
import random
import copy
from datetime import datetime

@pytest.fixture
def meta_set():
    return MetaSet()

def test_invalid_inputs(meta_set):
    with pytest.raises(TypeError):
        # Attempt to add a non-callable _meta_func
        meta_set._meta_func = "not callable"
        meta_set.add("example_value")
