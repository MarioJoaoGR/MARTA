
import pytest
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _CatchAllUndefinedParameters
from inspect import signature

# Mocking the original init method for testing purposes
def mock_original_init(self, *args, **kwargs):
    pass

class TestIgnoreInit:
    
    @pytest.mark.parametrize("obj, kwargs", [
        (None, {}),
        ([], {}),
        ({}, {'key': 'value'}),
        (123, {})
    ])
    def test_edge_cases(self, obj, kwargs):
        # Mock the original init method
        with pytest.raises(TypeError):
            _ignore_init = _IgnoreUndefinedParameters()
            init_signature = signature(mock_original_init)
            
            known_kwargs, _ = \
                _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                    obj, kwargs)
            num_params_takeable = len(init_signature.parameters) - 1  # don't count self
            args = []
            bound_parameters = init_signature.bind_partial(None, *args, **known_kwargs)
            bound_parameters.apply_defaults()
            
            arguments = bound_parameters.arguments
            arguments.pop("self", None)
            final_parameters = \
                _IgnoreUndefinedParameters.handle_from_dict(obj, arguments)
            mock_original_init(final_parameters)
