
# Importing the lazyproperty decorator from the correct module path
from pytutils.memo import lazyproperty

def test_edge_case():
    class MyClass:
        @lazyproperty
        def expensive_calculation(self):
            print("Calculating...")
            return sum(i**2 for i in range(1000))
    
    obj = MyClass()
    first_access = obj.expensive_calculation  # "Calculating..." should be printed
    assert hasattr(obj, '_lazy_expensive_calculation')  # Check if the attribute is cached
    second_access = obj.expensive_calculation  # No output, value is already computed and stored
    assert first_access == second_access  # Ensure the same value is returned without recalculating
