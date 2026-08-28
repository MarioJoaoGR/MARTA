
import pytest
from mimesis.builtins.pt_br import BrazilSpecProvider

# Test initialization without mask
def test_valid_input_with_mask():
    provider = BrazilSpecProvider()
    cnpj_number = provider.cnpj(with_mask=True)
    assert isinstance(cnpj_number, str), "Expected a string representation of CNPJ"
    assert len(cnpj_number) == 18, "Expected length of CNPJ to be 18 characters including mask"
    # Additional assertions can go here to validate the format and structure of the CNPJ number

# Test initialization with invalid input type