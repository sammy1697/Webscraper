import pandas as pd
import os

# Get the path to the directory containing the Excel files
excel_files_path = "C:/Users/samar/OneDrive/Documents/Work/JOBS/Belgium Jobs"

# Get a list of all the Excel files in the directory
excel_files = []
for file in os.listdir(excel_files_path):
    if file.endswith(".csv"):
        excel_files.append(file)

# Create a Pandas DataFrame to store the appended data
appended_df = pd.DataFrame()

# Iterate through the Excel files and append the data to the DataFrame
for excel_file in excel_files:

    # Read the Excel file into a Pandas DataFrame
    df = pd.read_excel(excel_file)

    # Remove the extension from the Excel file name
    excel_file_name = os.path.splitext(excel_file)[0]

    # Add a column to the DataFrame with the Excel file name
    df["Job Skill"] = excel_file_name

    # Append the DataFrame to the appended DataFrame
    appended_df = appended_df.append(df, ignore_index=True)

# Save the appended DataFrame to a CSV file
appended_df.to_csv("appended_data.csv", index=False)
