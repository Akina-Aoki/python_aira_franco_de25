# Error Handling in Python

Reference for managing and handling errors in Python code.  
Focus is on the use of `try` and `except` blocks, handling specific exception types, and preventing program crashes.

## Key Error Handling Concepts

### 1. Purpose of Error Handling

- Protect code from crashing on known or unknown errors.
- Provide custom messages or handling logic on error occurrence.

## Usage Guidelines

- Place known or risky code inside `try` blocks.
- Add specific `except` branches for anticipated exceptions (e.g., `NameError`, `ZeroDivisionError`).
- Include a final, generic `except` branch when a catch-all is needed.
- Use exception objects for diagnostics, if necessary.

---

## References

- [Python: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python: try and except Statements](https://docs.python.org/3/library/exceptions.html)
- [Python: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

---