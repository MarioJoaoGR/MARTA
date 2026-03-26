
import pytest
from string_utils.validation import is_credit_card

def test_empty_string():
    assert not is_credit_card('')
    assert not is_credit_card(' ')
    assert not is_credit_card('   ')
