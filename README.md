## XML to CSV Conversion
---

## Step-by-Step Code Breakdown

### 1. **Import Necessary Modules**

```python
import xml.etree.ElementTree as ET
import csv
import os
```

* `xml.etree.ElementTree`: Parses the XML file.
* `csv`: Writes tabular data into a `.csv` file.
* `os`: Helps access operating system features like file paths and current working directory.

---

### 2. **Print Current Working Directory (for Debugging)**

```python
print("Current working directory:", os.getcwd())
```

This line shows where Python is looking for `sample.xml`. Useful if you get a "file not found" error.

> If your XML file is **not** in this directory, you’ll need to update the path.

---

### 3. **Define XML File Path**

```python
xml_file_path = 'sample.xml'
```

Here, you define the name or path to your XML file. You can change this to:

* A full path: `'D:/mydata/sample.xml'`
* A relative path: `'./data/sample.xml'`

---

### 4. **Try to Parse the XML File**

```python
try:
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
```

* `ET.parse(...)`: Loads and parses the XML.
* `.getroot()`: Fetches the root element. In your case, it’s `<library>`.

If the file is not found, the `except` block below will catch the error.

---

### 5. **Open the Output CSV File**

```python
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
```

* Opens `output.csv` in **write mode**.
* `newline=''`: Prevents blank lines between rows (important on Windows).
* `encoding='utf-8'`: Ensures support for special characters.
* `csv.writer(csvfile)`: Creates a CSV writer object.

---

### 6. **Write the Header Row**

```python
        writer.writerow(['title', 'author', 'genre', 'year', 'publisher'])
```

* This is the **first row** in the CSV.
* It defines the column names to match the XML tags in each `<book>`.

---

### 7. **Loop Through `<book>` Elements and Extract Data**

```python
        for book in root.findall('book'):
```

* Loops through each `<book>` inside `<library>`.

Inside the loop:

```python
            title = book.find('title').text if book.find('title') is not None else ''
```

* `book.find('title')`: Searches for the `<title>` tag inside the current `<book>`.
* `.text`: Retrieves the actual text, like "Dolorem qui adipisci."
* `if ... is not None else ''`: Ensures the program doesn't crash if a tag is missing.

Repeat this for each field: `author`, `genre`, `year`, and `publisher`.

---

### 8. **Write the Data Row**

```python
            writer.writerow([title, author, genre, year, publisher])
```

* Writes one row to the CSV file for each `<book>` entry.

---

### 9. **Handle Missing File Error**

```python
except FileNotFoundError:
    print(f"Error: File '{xml_file_path}' not found.")
```

If the file doesn’t exist in the specified location, this block catches the exception and prints a friendly message instead of crashing.

---

---

## Summary of the Flow

| Step | What It Does                                  |
| ---- | --------------------------------------------- |
| 1    | Import modules                                |
| 2    | Show working directory for debugging          |
| 3    | Define path to your XML file                  |
| 4    | Parse the XML structure                       |
| 5    | Open CSV file for writing                     |
| 6    | Write header row to CSV                       |
| 7    | Loop through each `<book>` and extract fields |
| 8    | Write each book’s data to the CSV             |
| 9    | Gracefully handle missing file errors         |

---
