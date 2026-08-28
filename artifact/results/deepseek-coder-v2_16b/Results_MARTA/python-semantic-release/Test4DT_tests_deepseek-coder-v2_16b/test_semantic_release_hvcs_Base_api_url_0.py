
import pytest
from unittest.mock import patch
from abc import ABC

class Base(ABC):
    def api_url(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")

class SpecificAPI(Base):
    def api_url(self) -> str:
        return "https://api.example.com/endpoint"

# Test scenarios
def test_valid_case():
    instance = SpecificAPI()
    assert instance.api_url() == "https://api.example.com/endpoint"

def test_edge_case():
    class NoImplementation(Base):
        pass
    with pytest.raises(NotImplementedError):
        no_implementation_instance = NoImplementation()
        no_implementation_instance.api_url()

def test_error_case():
    class ErrorImplementation(Base):
        def api_url(self) -> str:
            raise NotImplementedError("Subclasses must implement this method")
    
    with patch.object(ErrorImplementation, 'api_url', lambda self: "https://api.example.com/endpoint"):
        error_instance = ErrorImplementation()
        assert error_instance.api_url() == "https://api.example.com/endpoint"
