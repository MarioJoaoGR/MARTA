
import pytest
from dataclasses_json import mm  # Assuming this is the correct module to import for Schema and _ExtendedEncoder

class TestSchemaDumps:
    @pytest.mark.parametrize("kwargs", [{}])
    def test_invalid_input_missing_cls_arg(self, kwargs):
        with pytest.raises(TypeError) as excinfo:
            # Assuming 'schema' is an instance of Schema that you want to serialize
            schema = mm.Schema()  # Create a dummy Schema instance for the purpose of this test
            schema.dumps(**kwargs)
        assert "missing 1 required positional argument" in str(excinfo.value)
