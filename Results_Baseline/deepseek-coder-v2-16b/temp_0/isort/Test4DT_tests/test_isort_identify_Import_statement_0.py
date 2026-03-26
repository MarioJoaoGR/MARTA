
# Module: isort.identify
# test_isort_identify.py
from isort.identify import Import


def test_basic_import():
    imp = Import(line_number=1, indented=True, module="my_module")
    assert imp.statement() == "import my_module"

def test_import_with_attribute():
    imp = Import(line_number=2, indented=False, module="mymodule", attribute="MyClass")
    assert imp.statement() == "from mymodule import MyClass"

def test_import_with_alias():
    imp = Import(line_number=3, indented=True, module="another_module", alias="am")
    assert imp.statement() == "import another_module as am"

def test_cimport_with_attribute_and_alias():
    imp = Import(line_number=4, indented=False, module="mymodule", attribute="MyClass", cimport=True, alias="mc")