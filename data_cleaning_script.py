"""
Data Cleaning Script

This script provide fuctions to automates common data cleaning tasks:
- Removing duplicates
- Standardizing column names
- Trimming whitespace from string columns
- Handling missing values
"""


# import necessary libraries
import pandas as pd

# This function remove duplicate rows
def drop_duplicate(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()


# This function standardize column names
def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert column names to lowercase, remove start & end white space(strips), and replace spaces with underscores.
    Example: " Age Group  " -> "age_group"
    """
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


# This function remove/trim whitespace from object type columns
def trim_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading/trailing whitespace in string columns."""
    str_cols = df.select_dtypes(include="object").columns
    for col in str_cols:
        df[col] = df[col].str.strip()
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
        "Student Name": [" Tom", " Jerry ", " Tom", "Ben "],
        "Age": [18, 20, 18, None],
        "City": ["Lagos", "Abuja ", "Lagos", " Kano"]
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    # Apply data cleaning script functions
    df = drop_duplicate(df)
    df = standardize_column_names(df)
    df = trim_whitespace(df)
    df = clean_missing_values(df, method="mean")

    print("\n Cleaned DataFrame:")
    print(df)
