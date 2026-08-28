
import pytest
from mimesis.builtins.en import USASpecProvider

def test_valid_input_mbti():
    provider = USASpecProvider()
    result = provider.personality('mbti')
    assert isinstance(result, str)
    assert result in ('ISFJ', 'ISTJ', 'INFJ', 'INTJ',
                      'ISTP', 'ISFP', 'INFP', 'INTP',
                      'ESTP', 'ESFP', 'ENFP', 'ENTP',
                      'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

def test_valid_input_rheti():
    provider = USASpecProvider()
    result = provider.personality('rheti')
    assert isinstance(result, int)
    assert 1 <= result <= 10
