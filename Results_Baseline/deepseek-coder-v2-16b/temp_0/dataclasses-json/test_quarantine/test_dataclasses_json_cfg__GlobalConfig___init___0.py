
# Module: dataclasses_json.cfg
import pytest
from typing import Dict, Type, Callable, Union, Optional
from marshmallow import fields as MarshmallowField

class _GlobalConfig:
    """
    A class to manage global configuration settings for encoders, decoders, and marshmallow fields.

    This class provides a mechanism to register and retrieve encoder, decoder, and marshmallow field mappings.

    Attributes:
        encoders (Dict[Union[type, Optional[type]], Callable]): A dictionary that maps types or None to callables for encoding data.
        decoders (Dict[Union[type, Optional[type]], Callable]): A dictionary that maps types or None to callables for decoding data.
        mm_fields (Dict[Union[type, Optional[type]], MarshmallowField]): A dictionary that maps types or None to Marshmallow fields.

    Examples:
        Initializes the GlobalConfig class with no parameters.
    """
    def __init__(self):
        self.encoders = {}
        self.decoders = {}
        self.mm_fields = {}

    def register_encoder(self, type_: Type, encoder: Callable) -> None:
        """
        Registers a callable to encode data for a specific type.
        
        :param type_: The type of data to be encoded.
        :param encoder: The callable that performs the encoding.
        """
        self.encoders[type_] = encoder

    def register_decoder(self, type_: Type, decoder: Callable) -> None:
        """
        Registers a callable to decode data for a specific type.
        
        :param type_: The type of data to be decoded.
        :param decoder: The callable that performs the decoding.
        """
        self.decoders[type_] = decoder

    def register_mm_field(self, type_: Type, field: MarshmallowField) -> None:
        """
        Registers a Marshmallow field for a specific type.
        
        :param type_: The type of data to which the field applies.
        :param field: The Marshmallow field object.
        """
        self.mm_fields[type_] = field

# Test cases for _GlobalConfig class methods
def test_register_encoder():
    config = _GlobalConfig()
    
    def custom_encoder(data):
        return f"Encoded {data}"
    
    config.register_encoder(int, custom_encoder)
    assert config.encoders[int]("123") == "Encoded 123"
    with pytest.raises(KeyError):
        config.encoders[str]("test")

def test_register_decoder():
    config = _GlobalConfig()
    
    def custom_decoder(encoded):
        return int(encoded.split()[-1])
    
    config.register_decoder(int, custom_decoder)
    assert config.decoders[int]("Encoded 123") == 123
    with pytest.raises(KeyError):
        config.decoders[str]("test")

def test_register_mm_field():
    config = _GlobalConfig()
    
    field = MarshmallowField()
    config.register_mm_field(str, field)
    assert config.mm_fields[str] == field
    with pytest.raises(KeyError):
        config.mm_fields[int]

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___0
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___0.py:79:12: E1102: MarshmallowField is not callable (not-callable)

"""