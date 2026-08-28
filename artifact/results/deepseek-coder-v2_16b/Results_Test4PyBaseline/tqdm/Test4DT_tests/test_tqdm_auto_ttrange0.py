
# Module: tqdm.auto
import pytest
from tqdm import tqdm
from tqdm.auto import trange  # Importing from tqdm.auto instead of tqdm directly

def test_trange_with_range():
    result = list(trange(10))
    assert len(result) == 10, "Expected a range of length 10"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"

def test_trange_with_range_and_desc():
    result = list(trange(10, desc="Testing"))
    assert len(result) == 10, "Expected a range of length 10"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"

def test_trange_with_range_and_unit():
    result = list(trange(10, unit="test"))
    assert len(result) == 10, "Expected a range of length 10"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"

def test_trange_with_range_and_desc_and_unit():
    result = list(trange(10, desc="Testing", unit="test"))
    assert len(result) == 10, "Expected a range of length 10"
    assert all(isinstance(i, int) for i in result), "All elements should be integers"
