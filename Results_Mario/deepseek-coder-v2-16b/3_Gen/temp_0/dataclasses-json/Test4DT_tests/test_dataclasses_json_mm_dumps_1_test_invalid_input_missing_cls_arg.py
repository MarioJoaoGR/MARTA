
import pytest
from dataclasses_json import mm  # Assuming this is the correct module to import for Schema and _ExtendedEncoder

class TestSchemaDumps:
    @pytest.mark.parametrize("kwargs", [{}])
    def test_invalid_input_missing_cls_arg(self, kwargs):
        with pytest.raises(TypeError) as excinfo:
            # Assuming 'schema_instance' is a valid instance of Schema for testing
            schema_instance = mm.Schema()  # Create an instance of the Schema class
            schema_instance.dumps(**kwargs)
        assert "missing 1 required positional argument" in str(excinfo.value)
