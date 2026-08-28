
# Module: ansible.utils._junit_xml
import pytest
from dataclasses import dataclass
import typing as t
import decimal
import xml.etree.ElementTree as ET
import dataclasses  # Importing dataclasses explicitly

@dataclass
class TestCase:
    name: str
    assertions: t.Optional[int] = None
    classname: t.Optional[str] = None
    status: t.Optional[str] = None
    time: t.Optional[decimal.Decimal] = None
    errors: t.List[t.Any] = dataclasses.field(default_factory=list)
    failures: t.List[t.Any] = dataclasses.field(default_factory=list)
    skipped: t.Optional[str] = None
    system_out: t.Optional[str] = None
    system_err: t.Optional[str] = None
    is_disabled: bool = False
    
    def is_error(self) -> bool:
        return bool(self.errors)
    
    def get_xml_element(self) -> ET.Element:
        element = ET.Element('testcase', {'name': self.name})
        
        if self.skipped:
            skipped_elem = ET.SubElement(element, 'skipped')
            skipped_elem.text = self.skipped
        
        for error in self.errors:
            error_elem = ET.SubElement(element, 'error', {'message': str(error)})
        
        if self.system_out:
            system_out_elem = ET.SubElement(element, 'system-out')
            system_out_elem.text = self.system_out
        
        if self.system_err:
            system_err_elem = ET.SubElement(element, 'system-err')
            system_err_elem.text = self.system_err
        
        return element

# Test cases for the TestCase class
def test_create_test_case():
    test_case = TestCase(name="example_test")
    assert test_case.name == "example_test"
    assert not test_case.is_error()

def test_add_error_to_test_case():
    test_case = TestCase(name="example_test")
    test_case.errors.append("An error occurred")
    assert test_case.is_error()

def test_generate_xml_representation():
    test_case = TestCase(name="example_test", system_err="System error message")
    element = test_case.get_xml_element()
    tree = ET.ElementTree(element)
    assert ET.tostring(tree.getroot(), encoding='unicode') == '<testcase name="example_test"><system-err>System error message</system-err></testcase>'

def test_is_error_method():
    test_case = TestCase(name="example_test")
    assert not test_case.is_error()
    
    test_case.errors.append("An error occurred")
    assert test_case.is_error()
