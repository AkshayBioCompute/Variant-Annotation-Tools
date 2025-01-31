import pandas as pd

# Load the TSV file into a DataFrame
file_path = r'D:\wellytics\test\VEP_result_ENSEMBL.txt'
df = pd.read_csv(file_path, sep='\t')

# Print column names to verify
print(df.columns)

# Define the columns to delete
columns_to_delete = ['#Uploaded_variation', 'Feature_type', 'Feature', 'BIOTYPE', 'EXON', 'INTRON',
                     'HGVSc', 'HGVSp', 'cDNA_position', 'CDS_position', 'Protein_position', 'Amino_acids',
                     'Codons', 'DISTANCE', 'FLAGS', 'SYMBOL_SOURCE', 'HGNC_ID', 'MANE_SELECT',
                     'MANE_PLUS_CLINICAL', 'TSL', 'APPRIS', 'SIFT', 'PolyPhen', 'MOTIF_NAME', 'MOTIF_POS',
                     'HIGH_INF_POS', 'MOTIF_SCORE_CHANGE', 'TRANSCRIPTION_FACTORS']

# Remove columns that exist in the DataFrame
columns_to_delete_existing = [col for col in columns_to_delete if col in df.columns]
df.drop(columns=columns_to_delete_existing, inplace=True)

# Remove duplicate rows based on the "gene" column, keeping the row with the highest "IMPACT" value
df.drop_duplicates(subset=["Gene"], keep='last', inplace=True)

# Save the modified DataFrame to a new TSV file
output_file_path = r'D:\wellytics\test\1.tsv'
df.to_csv(output_file_path, sep='\t', index=False)
