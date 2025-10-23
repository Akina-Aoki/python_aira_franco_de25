from numbers import Number

def validate_positive(value: Number):
    """Ensure the value is a positive number."""
    if not isinstance(value, Number):
        raise TypeError(f"Expected a number, got {type(value).__name__}")
    if value <= 0:
        raise ValueError(f"Expected a positive number, got {value}")
