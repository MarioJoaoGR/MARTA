
import pytest
from docstring_parser.google import GoogleParser

def test_edge_case():
    # Arrange
    parser = GoogleParser()
    
    # Act & Assert
    assert parser is not None, "GoogleParser instance should be created successfully"
