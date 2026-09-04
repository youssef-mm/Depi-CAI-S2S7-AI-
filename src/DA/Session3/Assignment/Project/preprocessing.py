import os
import pandas as pd

def read_data_file(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV dataset from the provided path safely.
    Handles FileNotFoundError, EmptyDataError, and invalid path exceptions.
    """
    if not isinstance(file_path, str) or not file_path.strip():
        raise ValueError("Invalid file path provided: Path must be a non-empty string.")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The dataset at path '{file_path}' was not found.")

    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.EmptyDataError:
        raise ValueError(f"Error: The file at '{file_path}' is empty.")
    except Exception as e:
        raise RuntimeError(f"Unexpected error occurred while reading the file: {e}")


def drop_unnecessary_features(df: pd.DataFrame, cols_to_drop: list) -> pd.DataFrame:
    """
    Removes columns provided through cols_to_drop from the DataFrame.
    Does not assume any specific column names.
    """
    if not isinstance(cols_to_drop, (list, tuple, set)):
        raise TypeError("cols_to_drop must be a list, tuple, or set of column names.")

    # Drop columns that actually exist in df to prevent errors
    existing_cols = [col for col in cols_to_drop if col in df.columns]
    return df.drop(columns=existing_cols)


def check_data_type(df: pd.DataFrame) -> pd.DataFrame:
    """
    Inspects dataset structure and returns a transposed report containing:
    - Data type
    - Number of unique values
    - Example/First non-null value (bonus clarity)
    """
    report = pd.DataFrame({
        "Datatype": df.dtypes.astype(str),
        "Unique_Values": df.nunique(),
        "Missing_Values": df.isnull().sum()
    })
    
    # Return transposed DataFrame for easy scanning
    return report.T