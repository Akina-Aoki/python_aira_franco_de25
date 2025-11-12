# Python Dictionaries: Reference and Guide

A practical reference for dictionaries in Python.  
Includes basics, common methods, updating entries, safe lookups, and usage in basic data cleaning.

## Best Practices

- Use `.get()` for safe key access if unsure the key will exist.
- For default empty values, using `collections.defaultdict()` is handy for counters/accumulation.

  ```python
  from collections import defaultdict
  d = defaultdict(int)
  d["dog"] += 1
  ```

- `.items()` is the best way to iterate over key-value pairs.
- Dictionary keys must be hashable (usually strings, numbers, tuples of immutables).

## References

- [Python Official: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [GeeksForGeeks: Python Dictionary](https://www.geeksforgeeks.org/python-dictionary/)