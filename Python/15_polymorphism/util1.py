from numbers import Number

def validate_number(value):
    """
    Validate that the given value is a number.

    Parameters
    ----------
    value : any type
        The value to check.

    Raises
    ------
    TypeError
        If the value is not a number (int or float).
    """
    if not isinstance(value, Number):   # checks if the value is a number
        raise TypeError(f"value must be a number, not {type(value)}")
