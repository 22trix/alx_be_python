# Define a Calculator class to demonstrate class and static methods
class Calculator:
    # Class attribute shared by all instances of the class
    calculation_type = "Arithmetic Operations"

    # Static method: does not need access to the class (cls) or an instance (self)
    @staticmethod
    def add(a, b):
        # Simply performs addition and returns the result
        return a + b

    # Class method: has access to the class itself through 'cls'
    @classmethod
    def multiply(cls, a, b):
        # Can use class attributes (like calculation_type)
        print(f"Calculation type: {cls.calculation_type}")
        # Performs multiplication and returns the result
        return a * b
