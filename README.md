# Variant-Annotation-Tools
# Annotation

## Directory Structure
The directory contains two folders:
- `vep`
- `vcfanno`

## VCF File
- **Input File:** `test1.vcf`

## VEP Annotation
The `test1.vcf` file was processed using **VEP** on a Windows system because the server couldn't support VEP annotation, leading to a failure midway through the process.

### VEP Command Used:
```sh
./vep --af --af_gnomade --af_gnomadg --appris --biotype --buffer_size 500 \
--check_existing --distance 5000 --mane --plugin GO,[path_to]/ --polyphen b \
--pubmed --regulatory --show_ref_allele --sift b --species homo_sapiens \
--symbol --transcript_version --tsl --uploaded_allele --cache \
--input_file [input_data] --output_file [output_file]
```

### Output Files:
- `New_vep.vcf`
- `VEP_result_ENSEMBL.txt`

### Analysis Steps:
#### 1. Filtering VEP Results
- **Python script:** `1_filter_vep.py`
- **Input File:** `VEP_result_ENSEMBL.txt`
- **Output File:** `1.tsv`
- **Purpose:** Removes unused columns for reporting purposes.

#### 2. Quality Control Filtering
- **Python script:** `2_QC_VEP.py`
- **Input File:** `1.tsv`
- **Output File:** `2.tsv`
- **Purpose:** Filters the `Consequence` column to retain missense variants and filters the `CLIN_SIG` column to retain variants according to ACMG guidelines (e.g., pathogenic, uncertain significance, etc.).

#### 3. Final Variant Selection
- **Python script:** `3_Final_variant.py`
- **Input File:** `2.tsv`
- **Output File:** `3.tsv`
- **Purpose:** Generates the final set of variants for reporting by filtering out rows with missing values and allele frequencies greater than 0.05.

---

## vcfAnno Annotation
- **VCF File:** `test2.vcf`
- **Executed on:** Linux system

### vcfAnno Command Used:
```sh
./vcfanno -lua /home/akkey/Akshay/wellytics/test/clinvar/vcfanno/example/clinvar.lua \
conf.toml test2.vcf > 1.vcf
```

### Output Files:
- `1.vcf`

The folder contains the `Clinvar.lua` and `conf.toml` files.

### Analysis Steps:
#### 4. Filtering vcfAnno Results
- **Python script:** `vcfanno_filter_clinvar.py`
- **Input File:** `1.vcf`
- **Output File:** `akj_vcfanno.tsv`
- **Purpose:** Extracts ClinVar details, though many blank entries are present. When opening the file in Excel, use filters to examine the ClinVar results. Additionally, gnomAD and dbSNP information is included but has not been filtered, as these were already obtained from VEP.

---

## Notes:
- Ensure that required dependencies and plugins are installed before running VEP and vcfAnno.
- Modify the `[path_to]` and `[input_data]` variables in the VEP command as per the file structure.
- Excel filtering is recommended for better visualization of ClinVar results.

---

**Maintainer:** Akshay Jain  
**Last Updated:** August 2024

