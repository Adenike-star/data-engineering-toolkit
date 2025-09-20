"""
Data Loading Script

This script provides functions to load/write transformed data into
different storage formats (Parquet, CSV, JSON).
"""

# Import necessary library
import pandas as pd
import json
import csv
import pyarrow.parquet as pq


# This function loads data to a Parquet file
def load_to_parquet(input_file: str, output_file: str):
    """
    Reads data from different formats and loads it into a Parquet file.

    Args:
        input_file --> str : Path to input file (df, CSV, Excel, JSON, Parquet supported).
        output_file --> str: Path where parquet file will be saved.
    """
    try:                                                  # wraps code so it won’t crash, if something fails
        if isinstance(input_file, pd.DataFrame):          # checks if the data is a pandas dataframe
            input_file.to_parquet(output_file, index=False)
        elif input_file.endswith(".csv"):                 # try to detect the file format by file extension & --> pull to dataframe --> Parquet
            df = pd.read_csv(input_file)
            df.to_parquet(output_file, index=False)
        elif input_file.endswith(".xlsx") or input_file.endswith(".xls"):
            df = pd.read_excel(input_file)
            df.to_parquet(output_file, index=False)
        elif input_file.endswith(".json"):
            df = pd.read_json(input_file)
            df.to_parquet(output_file, index=False)
        elif input_file.endswith(".parquet"):  
            df = pd.read_parquet(input_file) 
            df.to_parquet(output_file, index=False)          # already parquet, just re-save
        else: 
            raise ValueError("Unsupported file format. Use a DataFrame, CSV, Excel, JSON or Parquet.")
        # Success message
        print(f"Data successfully written to {output_file} (Parquet)")  
    except Exception as e:                                       # if anything goes wrong, it prints the error message
        print(f"Error writing to Parquet: {e}")


# This function loads df to a csv file
def load_df_to_csv(df: pd.DataFrame, output_file: str):
    """
    Save DataFrame to CSV file.

    Args:
        df: DataFrame containing data to save.
        output_file: Path to the output CSV file.
    """
    try:
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file} (CSV)")
    except Exception as e:
        print(f"Error saving to CSV: {e}")


# This function loads df to a json file
def load_df_to_json(df: pd.DataFrame, output_file: str):
    """
    Save DataFrame to a JSON file.

    Args:
        df: DataFrame containing data to save.
        output_file: Path to the output JSON file.
    """
    try:
        df.to_json(output_file, index=False)
        print(f"Data saved to {output_file} (JSON)")
    except Exception as e:
        print(f"Error saving to JSON: {e}")
 

 # This function loads data from json to df
def load_from_json(filename: str) -> pd.DataFrame:
    """
    Load data from a JSON file into a Pandas DataFrame.

    Args:
        filename: Path to the input JSON file.

    Returns:
        Pandas DataFrame containing the JSON data.
    """
    try:
        df = pd.read_json(filename)
        print(f"Data successfully loaded from {filename} (JSON)")
        return df
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return pd.DataFrame()                  # return empty DataFrame if error


# This function loads data from csv to df
def load_from_csv(filename: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a Pandas DataFrame.

    Args:
        filename: Path to the input CSV file.

    Returns:
        Pandas DataFrame containing the CSV data.
    """
    try:
        df = pd.read_csv(filename)
        print(f"Data successfully loaded from {filename} (CSV)")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return pd.DataFrame()  # return empty DataFrame if error



if __name__ == "__main__":
    
    # testing.. testing
    # create df
    data = {
        "student_name": ["Tom", "Jerry", "Tom", "Ben"],
        "age": [18, 20, 18, 19],
        "city": ["Lagos", "Abuja ", "Lagos", "Kano"]
    }
    df = pd.DataFrame(data)


    # Apply data loading script functions, load file as parquet
    df = load_to_parquet(df, "output.parquet")
    
    
