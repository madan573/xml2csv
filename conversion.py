import xml.etree.ElementTree as ET
import csv

# Parse the XML file
tree = ET.parse('xml2csv/sample.xml')
root = tree.getroot()

# Open the output CSV file
with open('xml2csv/output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    # Write the CSV header
    writer.writerow(['title', 'author', 'genre', 'year', 'publisher'])

    # Loop through each <book> element
    for book in root.findall('book'):
        title = book.find('title').text if book.find('title') is not None else ''
        author = book.find('author').text if book.find('author') is not None else ''
        genre = book.find('genre').text if book.find('genre') is not None else ''
        year = book.find('year').text if book.find('year') is not None else ''
        publisher = book.find('publisher').text if book.find('publisher') is not None else ''
        
        # Write the data row
        writer.writerow([title, author, genre, year, publisher])
