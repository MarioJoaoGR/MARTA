
import pytest
from tqdm.rich import FractionColumn

# Test Case 1: Basic instantiation with default parameters
def test_fraction_column_default():
    frac_col = FractionColumn()
    assert frac_col.unit_scale is False
    assert frac_col.unit_divisor == 1000

# Test Case 2: Instantiation with unit_scale set to True and custom unit_divisor
def test_fraction_column_with_params():
    frac_col = FractionColumn(unit_scale=True, unit_divisor=1000)
    assert frac_col.unit_scale is True
    assert frac_col.unit_divisor == 1000

# Test Case 3: Instantiation with default parameters and checking the repr method
def test_fraction_column_repr():
    frac_col = FractionColumn()
    expected_repr = f"FractionColumn(unit_scale={frac_col.unit_scale}, unit_divisor={frac_col.unit_divisor})"