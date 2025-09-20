"""
Data Transformation Script

This script provide functions for basic data transformation tasks
commonly seen in data engineering pipelines.
"""

# import necessary library
import pandas as pd


# This function rename columns
def rename_columns(df: pd.DataFrame, column_rename_map: dict) -> pd.DataFrame:
    """
    Rename columns in the DataFrame.
    
    Args:
        df: Input DataFrame
        column_rename_map: Dictionary of {old_column_name: new_column_name}
    
    Returns:
        Transformed DataFrame
    """
    try:
        return df.rename(columns=column_rename_map)
    except Exception as e:
        print(f"Error renaming columns: {e}")
        return df


# Function to drop columns
def drop_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Drop one or more columns from a DataFrame.

    Args:
        df: Input DataFrame
        columns: List of column names to drop
                  A single string "Age" → for one column
                  A list of strings (["Age", "Class"]) → for multiple columns

    Returns:
        DataFrame without the specified columns
    """
    try:
        df = df.drop(columns=columns, axis=1)               # axis=1, drops column
        print(f"{columns} dropped")
        return df
    except KeyError as e:
        print(f"Error dropping columns: {e}")
        return df


# This function cleanse missing values
def clean_missing_values(df: pd.DataFrame, method: str = "drop", fill_value=None) -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.

    Args:
        df: Input DataFrame.
        method: Missing values options.
              "drop": Remove rows with any missing values.
              "mode": Replace missing values with the column mode (categorical columns only).
              "mean": Replace missing values with the column mean (numeric columns only).
              "median": Replace missing values with the column median (numeric columns only).
    Returns:
        A DataFrame with missing values handled.
    """
    try:
        if method == "drop":
            df = df.dropna()
            print("Dropped rows with missing values.")

        elif method == "mode":
            df = df.fillna(df.mode().iloc[0])                         # pick first mode value in case it ties
            print("Filled missing values with column mode.")

        elif method == "mean":
            df = df.fillna(df.mean(numeric_only=True))
            print("Filled missing values with column mean.")

        elif method == "median":
            df = df.fillna(df.median(numeric_only=True))
            print("Filled missing values with column median.")

        else:
            raise ValueError("Unsupported method. Choose from 'drop', 'mode', 'mean', 'median'.")

        return df

    except Exception as e:
        print(f"Error handling missing values: {e}")
        return df




if __name__ == "__main__":

    # testing.. testing
    # create df
    data = {
        "SName": ["Tom", "Jerry", "Ben"],
        "Age": [18, 20, None],
        "City": ["Lagos", "Abuja", "Kano"],
        "Class": ["grade 12", "grade 12", "grade 12"]
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    # Apply data cleaning script functions
    df = rename_columns(df, {"SName": "student_name"})
    df = drop_columns(df, "Class")
    df = clean_missing_values(df, method="mean")

    print("\n Cleaned DataFrame:")
    print(df)
