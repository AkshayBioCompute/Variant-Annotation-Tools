
import csv

# Path to the input TSV file
input_file_path = r'D:\wellytics\test\1.tsv'

# Path to save the filtered TSV file
output_file_path = r'D:\wellytics\test\2.tsv'

# Open the input TSV file for reading
with open(input_file_path, 'r', newline='') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    
    # Open the output file for writing
    with open(output_file_path, 'w', newline='') as filtered_file:
        writer = csv.writer(filtered_file, delimiter='\t')
        
        # Write the header row to the output file
        header = next(reader)
        writer.writerow(header)
        
        # Iterate through each row in the input TSV file
        for row in reader:
            # Check if 'missense' is present in the third column
            if 'missense' in row[2] and 'benign' not in row[11]:
                # Write the row to the output file
                writer.writerow(row)

print("Filtered TSV file has been saved successfully.")