
# Module: mimesis.builtins.pt_br
import pytest
from mimesis import Person

def get_verifying_digit_cpf(cpf, peso):
    """Calculate the verifying digit for the CPF.

    :param cpf: List of integers with the CPF.
    :param peso: Integer with the weight for the modulo 11 calculate.
    :returns: The verifying digit for the CPF.
    """
    soma = 0
    for index, digit in enumerate(cpf):
        soma += digit * (peso - index)
    resto = soma % 11
    if resto == 0 or resto == 1 or resto >= 11:
        return 0
    return 11 - resto  

# Test cases for the function get_verifying_digit_cpf
def test_get_verifying_digit_cpf_basic():
    cpf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    peso = 10
    assert get_verifying_digit_cpf(cpf, peso) == 0

def test_get_verifying_digit_cpf_string_input():
    cpf = [int(digit) for digit in "123456789"]
    peso = 10
    assert get_verifying_digit_cpf(cpf, peso) == 0

def test_get_verifying_digit_cpf_known_digits():
    cpf = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    peso = 10
    assert get_verifying_digit_cpf(cpf, peso) == 0
