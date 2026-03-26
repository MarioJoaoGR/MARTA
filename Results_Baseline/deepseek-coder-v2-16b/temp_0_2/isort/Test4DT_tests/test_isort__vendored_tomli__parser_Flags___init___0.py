
from typing import Dict

import pytest

from isort._vendored.tomli._parser import Flags


def test_initialization():
    flags = Flags()
    assert flags._flags == {}, "Initialization should result in an empty dictionary."

def test_set_for_relative_key():
    flags = Flags()
    flags.set_for_relative_key(["a", "b"], ["c"], Flags.EXPLICIT_NEST)