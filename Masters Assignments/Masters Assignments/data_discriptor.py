class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = "_" + name  # private backing attribute, unique per field

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Expected {self.expected_type.__name__}, got {type(value).__name__}"
            )
        setattr(instance, self.name, value)

class User:
    age = Typed(int)
    name = Typed(str)

