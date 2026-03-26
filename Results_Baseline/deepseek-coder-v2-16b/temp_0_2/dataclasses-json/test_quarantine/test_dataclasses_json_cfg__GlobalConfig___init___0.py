
import pytest
from typing import Dict, Callable, Union, Optional
from marshmallow import fields as MarshmallowField
import json

# Importing necessary modules
class _GlobalConfig:
    def __init__(self):
        self.encoders: Dict[Union[type, Optional[type]], Callable] = {}
        self.decoders: Dict[Union[type, Optional[type]], Callable] = {}
        self.mm_fields: Dict[Union[type, Optional[type]], MarshmallowField] = {}

    def register_encoder(self, type_, encoder):
        self.encoders[type_] = encoder

    def register_decoder(self, type_, decoder):
        self.decoders[type_] = decoder

    def register_mm_field(self, type_, mm_field):
        self.mm_fields[type_] = mm_field

# Example usage
config = _GlobalConfig()

def encoder(data):
    return json.dumps(data)

def decoder(data):
    return json.loads(data)

from marshmallow import fields  # Corrected indentation and syntax

# Registering an encoder for the dict type
config.register_encoder(dict, encoder)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================

"""