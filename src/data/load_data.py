import pandas as pd
import os
import glob


def load_data():
    # Set the paths
    template_path = f"{os.getcwd()}/../utils/dataset_template.csv"
    processed_data_path = f"{os.getcwd()}/../data/processed"  # when running locally switch to \\ instead of / in case of an error

    # Load the template file
    template_df = pd.read_csv(template_path)

    # Get all CSV files in the processed data directory that match the template
    csv_files = glob.glob(f"{processed_data_path}/*.csv")
    print("csv_files: ", csv_files)

    # List to store DataFrames
    dfs = []

    # Iterate through the CSV files and load them if they match the template
    for csv_file in csv_files:
        # Load each CSV file
        df = pd.read_csv(csv_file)

        # Check if the file matches the template (compare columns)
        if df.columns.equals(template_df.columns):
            dfs.append(df)

    # Concatenate all DataFrames into one
    if len(dfs) > 0:
        final_df = pd.concat(dfs, ignore_index=True)
    else:
        final_df = pd.DataFrame()

    return final_df
