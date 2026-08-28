
# test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py
import pytest
from py_backwards.utils.helpers import VariablesGenerator


def test_unique_generation():
    generator = VariablesGenerator()
    assert generator.generate("var1") != generator.generate("var2")
    assert generator.generate("var3") != generator.generate("var4")