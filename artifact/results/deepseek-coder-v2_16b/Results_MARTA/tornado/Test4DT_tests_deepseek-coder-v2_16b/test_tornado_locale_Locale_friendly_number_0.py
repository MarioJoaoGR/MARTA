
import pytest
from tornado.locale import Locale







def test_invalid_input_friendly_number():
    with pytest.raises(NotImplementedError):
        Locale(code="es_ES").friendly_number(123456789)
    
    with pytest.raises(NotImplementedError):
        Locale(code="fr_FR").friendly_number(123456789)