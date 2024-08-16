# Path to the CSV file
input_file_path = r"D:\Work\NLP\Project\Project\Thai_Word.csv"
# Path to the new file
output_file_path = r"D:\Work\NLP\Project\Project\Sorted_Thai_Word.csv"

# Read the CSV file into a list of rows
with open(input_file_path, 'r', encoding='utf-8') as file:
    rows = file.readlines()

# Sort the rows based on the number of characters before the first comma
sorted_rows = sorted(rows, key=lambda x: len(x.split(',')[0]), reverse=True)

# Write the sorted rows to a new file
with open(output_file_path, 'w', encoding='utf-8') as outfile:
    for row in sorted_rows:
        outfile.write(row)
