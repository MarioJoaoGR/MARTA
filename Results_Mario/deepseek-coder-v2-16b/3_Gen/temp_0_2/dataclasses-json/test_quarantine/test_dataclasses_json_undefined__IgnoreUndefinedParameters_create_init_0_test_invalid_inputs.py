
import inspect
import functools
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _CatchAllUndefinedParameters

class _IgnoreUndefinedParameters:
    """
    This class contains a method that creates an alternative initializer for the given object. The new initializer ignores undefined parameters and does nothing when they are encountered. It ensures that only known and defined parameters are used in the initialization process.
    
    Parameters:
        obj (object): The object whose initializer is to be modified.
        
    Returns:
        Callable: A function that serves as a new initializer for the given object, handling undefined parameters gracefully by ignoring them.
        
    Example:
        To use this class and its method, you would typically create an instance of it and call the `create_init` method with the desired object. For example:
        
        ```python
        from your_module import _IgnoreUndefinedParameters
        
        # Assuming 'MyClass' is a class that might have undefined parameters
        my_class_instance = MyClass()
        new_initializer = _IgnoreUndefinedParameters().create_init(my_class_instance)
        
        # Now you can use the modified initializer for your class instances:
        my_class_instance.__init__ = new_initializer
        ```
    """
    def create_init(obj) -> Callable:
        original_init = obj.__init__
        init_signature = inspect.signature(original_init)

        @functools.wraps(obj.__init__)
        def _ignore_init(self, *args, **kwargs):
            known_kwargs, _ = \
                _CatchAllUndefinedParameters._separate_defined_undefined_kvs(
                    obj, kwargs)
            num_params_takeable = len(
                init_signature.parameters) - 1  # don't count self
            num_args_takeable = num_params_takeable - len(known_kwargs)

            args = args[:num_args_takeable]
            bound_parameters = init_signature.bind_partial(self, *args,
                                                           **known_kwargs)
            bound_parameters.apply_defaults()

            arguments = bound_parameters.arguments
            arguments.pop("self", None)
            final_parameters = \
                _IgnoreUndefinedParameters.handle_from_dict(obj, arguments)
            original_init(self, **final_parameters)

        return _ignore_init

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_inputs.py:6:0: E0102: class already defined line 4 (function-redefined)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_inputs.py:30:4: E0213: Method 'create_init' should have "self" as first argument (no-self-argument)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_inputs.py:30:28: E0602: Undefined variable 'Callable' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_create_init_0_test_invalid_inputs.py:51:16: E1101: Class '_IgnoreUndefinedParameters' has no 'handle_from_dict' member (no-member)


"""