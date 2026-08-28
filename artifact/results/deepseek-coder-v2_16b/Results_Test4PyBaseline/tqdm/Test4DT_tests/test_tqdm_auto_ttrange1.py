# Module: tqdm.auto
import pytest
from tqdm import tqdm
from tqdm.auto import trange

# Test case for the trange function with a range of 10 items
def test_trange_with_range():
    result = list(trange(10))
    assert len(result) == 10, "Expected length of 10"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"

# Test case for the trange function with a range of 5 items and a custom unit
def test_trange_with_custom_unit():
    result = list(trange(5, unit="iteration"))
    assert len(result) == 5, "Expected length of 5"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"

# Test case for the trange function with a range of 20 items and a custom description
def test_trange_with_custom_description():
    result = list(trange(20, desc="Processing"))
    assert len(result) == 20, "Expected length of 20"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"

# Test case for the trange function with a range of 30 items and both custom unit and description
def test_trange_with_all_customs():
    result = list(trange(30, unit="step", desc="Executing"))
    assert len(result) == 30, "Expected length of 30"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"
