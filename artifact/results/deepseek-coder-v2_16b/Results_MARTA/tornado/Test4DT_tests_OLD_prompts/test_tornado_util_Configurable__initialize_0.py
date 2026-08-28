
import pytest
from tornado.util import Configurable



def test_invalid_configuration():
    class InvalidImplementation(Configurable):
        def configurable_base():
            return Configurable

        def initialize(self, *args, **kwargs):
            assert args == ()
            assert kwargs == {}
            print("Initializing InvalidImplementation instance with:", args, kwargs)

    # Configure the implementation subclass and keyword arguments
    with pytest.raises(TypeError):  # Ensure configure is not called directly
        Configurable.configure(impl_class=InvalidImplementation, impl_kwargs={'invalid': 'config'})