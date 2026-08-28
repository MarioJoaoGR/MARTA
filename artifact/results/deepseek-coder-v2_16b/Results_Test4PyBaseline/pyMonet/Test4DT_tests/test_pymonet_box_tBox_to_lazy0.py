
# Module: pymonet.box
# test_pymonet_box.py
from pymonet.box import Box
import pytest

@pytest.fixture
def int_box():
    return Box(42)

@pytest.fixture
def str_box():
    return Box("Hello, World!")

@pytest.fixture
def list_box():
    return Box([1, 2, 3])

def test_int_box_to_lazy(int_box):
    lazy_box = int_box.to_lazy()
    assert lazy_box.get() == 42

def test_str_box_to_lazy(str_box):
    lazy_box = str_box.to_lazy()
    assert lazy_box.get() == "Hello, World!"

def test_list_box_to_lazy(list_box):
    lazy_box = list_box.to_lazy()
    assert lazy_box.get() == [1, 2, 3]
