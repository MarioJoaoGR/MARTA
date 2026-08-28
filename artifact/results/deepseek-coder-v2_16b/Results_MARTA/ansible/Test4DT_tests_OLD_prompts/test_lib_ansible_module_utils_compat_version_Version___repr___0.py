
from lib.ansible.module_utils.compat.version import StrictVersion
import pytest
from unittest.mock import patch, MagicMock



def test_comparison():
    v1 = StrictVersion('1.2.3')
    v2 = StrictVersion('1.2.4')
    v3 = StrictVersion('1.2.3b4')
    v4 = StrictVersion('1.2.3')
    
    assert not (v1 == v2)
    assert v1 < v2
    assert v1 <= v2
    assert not (v1 > v2)
    assert not (v1 >= v2)
    
    assert not (v3 == v4)
    assert v3 < v4
    assert v3 <= v4
    assert not (v3 > v4)
    assert not (v3 >= v4)