# Python Unit Testing: Vectors
Manual and automated unit testing on a custom vector class in Python.

## Project Structure

16_unit_testing/
    |- manual_test.ipynb      # Manual notebook tests of Vector
    |- test_vector.py         # Automated pytest test suite
    |- vector.py              # Vector class implementation
    README.md

## Manual Testing

See `manual_test.ipynb` for step-by-step interactive checks:

- **Initialization**: Create vectors; inspect their `.numbers` property and representation.
- **Addition & Subtraction**: Try valid and invalid vector operations.
- **Type Checking**: Ensure errors are raised for wrong types (str, mismatched lengths).
- **Virtual Environment Setup**: Use screenshots and command walk-through for env setup and running tests.

Code sample (from notebook):

```python
from vector import Vector

v1 = Vector(2, 5)
print(v1.numbers)  # (2.0, 5.0)

v2 = Vector(1, 1)
print(v1 + v2)     # Vector(3.0, 6.0)

try:
    Vector("1", 3)
except TypeError as err:
    print(err)

try:
    v1 + Vector(1, 2, 3)
except TypeError as err:
    print(err)
```


## Automated Testing (pytest)

See `test_vector.py` for robust unit tests:

- **Initialization**: Valid/invalid creation of vectors.
- **Negative Values**: Test support for negatives.
- **Type Checking**: Fail on string input.
- **Length Checks**: `len()` works for various sizes.
- **Norm (`abs`)**: Test vector magnitude calculation.
- **Error Handling**: Empty vector raises `ValueError`.

Sample Pytest test:

```python
from vector import Vector
import math
from pytest import raises, approx

def test_valid_init():
    v = Vector(1, 2)
    assert v.numbers == (1, 2)

def test_negative_valid_init():
    v = Vector(-1, -5, 3)
    assert v.numbers == (-1, -5, 3)

def test_string_in_init_fails():
    with raises(TypeError):
        Vector("1")

def test_vector_norm_valid():
    v = Vector(1, 4)
    expected_norm = math.sqrt(v[0]**2 + v[1]**2)
    assert abs(v) == approx(expected_norm)
```

To run:

```sh
# (activate virtualenv as shown in notebook)
pytest --version
cd 16_unit_testing
pytest
```

## Vector Implementation

Reference for what is being tested (see `vector.py`):

- Supports arbitrary size vectors, numeric validation.
- Operator overloading: `+`, `-`, `*`, indexing, abs, repr.
- Type and length safety in math operations.
- Optional 2D plotting via matplotlib.
- Extensive inline docstrings for understanding.

---

## Best Practices

- Write both interactive manual checks and automated unit tests.
- Always assert correct exceptions for invalid inputs.
- Use Python built-in error types for clarity.
- Prefer `pytest` for simple, powerful test-writing.
- Document your methods and tests for clarity.

---

## References

- [pytest Documentation](https://docs.pytest.org/en/latest/)
- [Python Unit Testing (realpython)](https://realpython.com/python-testing/)
- [Vector Math - Wikipedia](https://en.wikipedia.org/wiki/Euclidean_vector)
- [PEP 8: Python Style Guide](https://peps.python.org/pep-0008/)