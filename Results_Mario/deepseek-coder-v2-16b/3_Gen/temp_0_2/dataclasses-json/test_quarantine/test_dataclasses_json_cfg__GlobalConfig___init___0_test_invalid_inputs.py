
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Union, Optional, Callable, Any
from marshmallow import MarshmallowField
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class _GlobalConfig:
    """
    A class to manage global configuration settings for encoders, decoders, and marshmallow fields.

    This module provides a simple way to serialize and deserialize dataclass instances to and from JSON, with support for nested dataclass structures. It is built on top of the excellent [marshmallow](https://github.com/marshmallow-code/marshmallow/) library.

    The `dataclasses_json` module includes a decorator `@dataclass_json` that automatically adds methods to serialize and deserialize instances of dataclass. It supports nested dataclass structures, including lists and dictionaries. Customizing how specific types are encoded and decoded can be achieved using encoders and decoders.

    Attributes:
        encoders (Dict[Union[type, Optional[type]], Callable]): A dictionary that maps types or None to callables for encoding data.
        decoders (Dict[Union[type, Optional[type]], Callable]): A dictionary that maps types or None to callables for decoding data.
        mm_fields (Dict[Union[type, Optional[type]], MarshmallowField]): A dictionary that maps types or None to Marshmallow fields.

    Methods:
        register_encoder(type, callable): Registers a callable as an encoder for a specific type or None.
        register_decoder(type, callable): Registers a callable as a decoder for a specific type or None.
        register_mm_field(type, MarshmallowField): Registers a Marshmallow field for a specific type or None.

    Examples:
        >>> config = _GlobalConfig()
        >>> def encoder(data):
        ...     return json.dumps(data)
        >>> config.register_encoder(int, encoder)
        >>> print(config.encoders[int])  # Outputs the registered encoder function for int type

    For more detailed documentation, including examples and advanced usage, please refer to the [official documentation](https://lidatong.github.io/dataclasses-json/).
    """
    encoders: Dict[Union[type, Optional[type]], Callable] = None
    decoders: Dict[Union[type, Optional[type]], Callable] = None
    mm_fields: Dict[Union[type, Optional[type]], MarshmallowField] = None

    def register_encoder(self, type_: Union[type, Optional[type]], callable_: Callable) -> None:
        if self.encoders is None:
            self.encoders = {}
        self.encoders[type_] = callable_

    def register_decoder(self, type_: Union[type, Optional[type]], callable_: Callable) -> None:
        if self.decoders is None:
            self.decoders = {}
        self.decoders[type_] = callable_

    def register_mm_field(self, type_: Union[type, Optional[type]], mm_field: MarshmallowField) -> None:
        if self.mm_fields is None:
            self.mm_fields = {}
        self.mm_fields[type_] = mm_field

# Test case for invalid inputs
def test_invalid_inputs():
    config = _GlobalConfig()
    
    # Check that register_* methods raise AttributeError when called on an instance without initialization
    with pytest.raises(AttributeError):
        config.register_encoder(int, lambda x: x)
    with pytest.raises(AttributeError):
        config.register_decoder(str, lambda y: y)
    with pytest.raises(AttributeError):
        config.register_mm_field(float, MarshmallowField())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_cfg__GlobalConfig___init___0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_cfg__GlobalConfig___init___0_test_invalid_inputs.py:5:0: E0611: No name 'MarshmallowField' in module 'marshmallow' (no-name-in-module)


"""