import pandas as pd

# Read the VCF file into a DataFrame
vcf_file = r"D:\test\1.vcf"
df = pd.read_csv(vcf_file, sep='\t', comment='#', header=None)

# Define column names
columns = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'patient1_normal_sample', 'Clinvar_significance']

# Remove 37125 rows
df = df.iloc[37124:]

# Filter out rows where INFO column is blank
df = df[df[7] != '.']

# Extract 'clinvar_clinical_significance' value from INFO column
df['Clinvar_significance'] = df[7].str.extract(r'clinvar_pathogenic=([^;]+)')

# Add column names
df.columns = columns

# Save the DataFrame to CSV
csv_file = r"D:\test\akj_vcfanno.csv"
df.to_csv(csv_file, index=False)

print("Conversion completed successfully. CSV file saved as:", csv_file)
