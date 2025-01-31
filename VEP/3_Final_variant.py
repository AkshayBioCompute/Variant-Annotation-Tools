import csv

file_path = r'D:\wellytics\test\2.tsv'
output_file_path = r'D:\wellytics\test\3.tsv'

def is_numeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

with open(file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    header = next(reader)
    writer = csv.writer(outfile, delimiter='\t')
    writer.writerow(header)
    for row in reader:
        if row[10].replace('-', '') != '' and is_numeric(row[10]) and float(row[10]) <= 0.05:
            row[10] = row[10].replace('-', '')
            writer.writerow(row)