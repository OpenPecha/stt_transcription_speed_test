import csv
import pandas as pd

# Lists to store the final distribution
files_1 = []
files_2 = []
files_3 = []

current_table = []

# Read and process the input data
with open('input_data.txt', 'r') as f:
    for line in f:
        # Skip separator lines
        if '|---' in line:
            continue
        
        # When we hit a header line, process the previous table and start a new one
        if '| File Name |' in line:
            # Process the previous table if it exists
            if current_table:
                # Distribute the rows from current table
                for i, row in enumerate(current_table):
                    if i == 0:
                        files_1.append(row)
                    elif i == 1:
                        files_2.append(row)
                    elif i == 2:
                        files_3.append(row)
            # Reset for new table
            current_table = []
            continue
        
        # Process data lines
        if '|' in line:
            parts = line.split('|')
            if len(parts) >= 2:
                filename = parts[1].strip()
                if filename and 'File Name' not in filename:
                    current_table.append(filename)
    
    # Process the last table
    if current_table:
        for i, row in enumerate(current_table):
            if i == 0:
                files_1.append(row)
            elif i == 1:
                files_2.append(row)
            elif i == 2:
                files_3.append(row)

# Read the parquet file
df = pd.read_parquet("hf://datasets/ganga4364/garchen_rinpoche_benchmark_result/data/train-00000-of-00001.parquet")

# Function to write CSV with matching rows from parquet
def write_csv_with_data(filenames, output_file):
    # Filter the dataframe for matching filenames
    matching_rows = df[df['file_name'].isin(filenames)]
    
    # Write to CSV
    matching_rows = matching_rows[['file_name', 'url', 'audio_duration', 'uni', 'inference_transcript', 'inference_checkpoint-19000']]
    matching_rows.to_csv(output_file, index=False)

# Write to CSV files with corresponding parquet data
write_csv_with_data(files_1, 'files_1.csv')
write_csv_with_data(files_2, 'files_2.csv')
write_csv_with_data(files_3, 'files_3.csv')
