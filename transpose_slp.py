import pandas as pd

# Specify the path to your input Excel file
input_file = 'Alberta SLP.xlsx'  # Make sure the file is in the current directory or provide the full path
output_file = 'transformed_data.xlsx'  # Name of the output file

# Read the Excel file, assuming data is in the first column of the first sheet.
# Adjust the `usecols` parameter if your data is located in a different column.
df = pd.read_excel(input_file, header=None, usecols=[0])

# Function to shift non-blank data up in each column
def shift_data_up(column):
    # Drop the empty cells and reset index without adding a new column
    return column.dropna().reset_index(drop=True)

# Apply the function to the DataFrame
df = df.apply(shift_data_up)

# Prepare a list to hold dictionaries for each row of data
data_list = []

# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Convert the cell to string to avoid AttributeError
    cell_value = str(row[0])
    
    # Assuming each entry in the cell is separated by newline
    entries = cell_value.split('\n')
    entry_dict = {}
    for entry in entries:
        if ': ' in entry:
            # Split each entry by the first occurrence of ": " to separate key and value
            key, value = entry.split(': ', 1)
            entry_dict[key.strip()] = value.strip()
    if entry_dict:  # Check if the dictionary is not empty
        data_list.append(entry_dict)

# Convert the list of dictionaries to a DataFrame
transformed_df = pd.DataFrame(data_list)

# Fill NaN with empty strings if any
transformed_df = transformed_df.fillna('')

# Save the DataFrame to a new Excel file
transformed_df.to_excel(output_file, index=False)

print(f"Data transformation complete. Check the '{output_file}' file.")
