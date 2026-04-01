
import pytest
from isort.deprecated.finders import FindersManager, BaseFinder, Config

class CustomFinder(BaseFinder):
    def find(self, module_name: str):
        if module_name == "valid_module":
            return "section"
        return None

def test_valid_input():
    class Config:
        verbose = False
    
    config = Config()
    custom_finders = [CustomFinder]
    
    manager = FindersManager(config=config, finder_classes=custom_finders)
    assert manager.find("valid_module") == "section"
