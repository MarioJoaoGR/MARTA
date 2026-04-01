
from dataclasses_json.exceptions import ValidationError
import datetime

class _IsoField:
    def __init__(self, required=True):
        self.required = required
        self.default_error_messages = {
            "required": "This field is required"
        }

    def _serialize(self, value, attr, obj, **kwargs):
        """
        Serializes a datetime object to an ISO formatted string.

        Parameters:
            value (datetime): The datetime object to be serialized.
            attr (str): The attribute name of the datetime field.
            obj: The object containing the datetime field.
            **kwargs: Additional keyword arguments.

        Returns:
            str or None: An ISO formatted string representation of the datetime if the value is not None, otherwise returns None if the field is optional and no value is provided, or raises a ValidationError with a "required" message if the field is required but no value is provided.

        Examples:
            To serialize a datetime object named `dt`:
            ```python
            serialized_dt = _serialize(dt, attr="datetime_field", obj=some_object)
            print(serialized_dt)  # Output will be an ISO formatted string like '2023-10-05T12:34:56'
            ```

            To handle optional fields where no value is provided:
            ```python
            serialized_optional = _serialize(None, attr="optional_field", obj=some_object)
            print(serialized_optional)  # Output will be None
            ```

            Handling a required field without providing a value:
            ```python
            try:
                _serialize(None, attr="required_field", obj=some_object)
            except ValidationError as e:
                print(e.message)  # Output will be the "required" message from the default error messages.
            ```

        Notes:
            - The function assumes that `value` is a datetime object, and it serializes it to an ISO formatted string using the `.isoformat()` method of the datetime module.
            - If the value is None and the field is optional (checked via `self.required`), the function returns None.
            - If the value is None and the field is required, a ValidationError with a "required" message is raised.
            - The function can be used in contexts where datetime objects need to be serialized into a string format that includes date and time information following ISO 8601 standards.
        """
        if value is not None:
            return value.isoformat()
        else:
            if not self.required:
                return None
            else:
                raise ValidationError(self.default_error_messages["required"])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__IsoField__serialize_1_test_required_field_missing
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_1_test_required_field_missing.py:2:0: E0401: Unable to import 'dataclasses_json.exceptions' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__IsoField__serialize_1_test_required_field_missing.py:2:0: E0611: No name 'exceptions' in module 'dataclasses_json' (no-name-in-module)


"""