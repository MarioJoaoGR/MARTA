
import pytest
from pytutils.memo import cachedmethod, _default
from functools import partial
from cachetools import cachedmethod as cm
import warnings

def test_invalid_inputs():
    with pytest.raises(NameError):
        @cachedmethod(lambda inst: {}, key=lambda inst, *args: args[0])
        def method(self):
            pass
