# Python Inheritance: Reference and Guide

Includes fundamentals, advanced composition, best practices, and sample code with industry-grade comments and docstrings.

14_Inheritance/
    |- Inheritance.ipynb                             # Parent & child classes, composition, validation
    |- UnitConverter_class_version.ipynb             # Applied class design, setter validation
    |- util.py                                       # Utility validation function
    |- oldcoins.py                                   # OldCoinsStash composition class
    |- dna_raw.txt                                   # (Sample data for possible extension)
    README.md

## Best Practices

- Always use docstrings for every class and public method.
- Use `super()` to guarantee correct constructor chaining.
- Prefer composition for extending functionality safely.
- Encapsulate data and validation with property setters/getters.
- Never expose sensitive or internal attributes directly (use underscores).
- Design flexible class interfaces for realistic, scalable software.
- Provide custom `__repr__` for debugging, and leverage Python's OOP idioms.

## References

- [Python Official Documentation: Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Real Python: Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- [Python Docstring Guide (PEP 257)](https://peps.python.org/pep-0257/)
- [Best Practices in OOP - StackOverflow](https://stackoverflow.com/questions/8685684/python-best-oop-practices)
- [Unit Testing OOP Systems (pytest guide)](https://docs.pytest.org/en/7.1.x/examples/test_class.html)
