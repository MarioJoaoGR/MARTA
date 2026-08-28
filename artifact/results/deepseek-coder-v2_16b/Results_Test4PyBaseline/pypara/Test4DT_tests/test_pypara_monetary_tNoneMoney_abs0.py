
import pytest
from pypara.monetary import NoneMoney

# Test creating an instance of NoneMoney
def test_create_nonemoney():
    nm = NoneMoney()
    assert isinstance(nm, NoneMoney)

# Test using the abs method
def test_abs_method():
    nm = NoneMoney()
    assert abs(nm) == nm

# Test using the __bool__ method
def test_bool_method():
    nm = NoneMoney()
    if bool(nm):
        print("Defined")
    else:
        print("Undefined")  # Outputs: Undefined

# Test comparing instances
def test_equality():
    nm1 = NoneMoney()
    nm2 = NoneMoney()
    assert nm1 == nm2

# Test converting to float
def test_float_conversion():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        float(nm)

# Test converting to int
def test_int_conversion():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        int(nm)

# Test negating the instance
def test_negation():
    nm = NoneMoney()
    neg_nm = -nm
    assert neg_nm == nm

# Test adding two instances
def test_addition():
    nm1 = NoneMoney()
    nm2 = NoneMoney()
    sum_nm = nm1 + nm2
    assert not sum_nm.__bool__()

# Test subtracting two instances
def test_subtraction():
    nm1 = NoneMoney()
    nm2 = NoneMoney()
    diff_nm = nm1 - nm2
    assert not diff_nm.__bool__()

# Test multiplying by a number
def test_multiplication():
    nm = NoneMoney()
    mul_nm = nm * 2