import csv

with open('my-csv-file.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Date', 'Class'])
    writer.writerow(['Timothy Unkert', '9/29/22', 'AP Calculus'])
    writer.writerow(['Sean', '9/29/22', 'Python'])
