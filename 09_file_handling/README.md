# File Handling in Python

Reference guide for handling text files in Python.  
Covers reading, writing, data cleaning, and best practices for efficient file management.

## Core Concepts

### 1. Reading Files

#### Open a file for reading
```python
f = open("test.txt", "r")
text = f.read()
print(text)
f.close()
```
- Always close the file after reading to release system resources.

#### Use `with` statement (recommended)
```python
with open("test.txt", "r") as f:
    text = f.read()
# File is closed automatically after exiting the block.
print(text)
```
- The `with` statement ensures that the file closes properly, even if errors occur.

---

### 2. Reading Files: Line by Line

```python
with open("quotes.txt", "r") as f_read:
    for quote in f_read:
        print(quote)
```
- Looping over a file object returns each line, including newline characters.

---

### 3. Data Cleaning and Manipulation

#### Remove leading/trailing whitespace and newlines
```python
quote = quote.strip(" ")   # Removes leading/trailing spaces
quote = quote.strip("\n")  # Removes newlines
```

#### Replace multiple spaces with a single space using regex
```python
import re
quote = re.sub(" +", " ", quote)
```

- The `re.sub()` function replaces patterns in a string.
- `" +"` matches any sequence of one or more spaces.

---

### 4. Writing to a New File

#### Write cleaned data to a new file
```python
import re

i = 1
with open("quotes.txt", "r") as f_read, open("quotes_cleaned.txt", "w") as f_write:
    for quote in f_read:
        quote = quote.strip(" ")
        quote = quote.strip("\n")
        quote = re.sub(" +", " ", quote)
        print(quote)  # Optional: Console output for verification
        if quote != "":
            f_write.write(f"{i},{quote}\n")
            i += 1
```
- Simultaneously open source file for reading and destination file for writing.
- Each cleaned quote is written as a CSV-style record: `row_number,quote`.

---

## File Examples

**test.txt** — Sample content for basic file operations.
```
random
text
file
```

## Best Practices

- Always use the `with` statement for file operations.
- Close files explicitly if not using `with`.
- Clean data as needed before downstream processing or analysis.

## References

- [Python Official: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Official: Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [GeeksForGeeks: Python String Methods](https://www.geeksforgeeks.org/python/python-string-methods/)