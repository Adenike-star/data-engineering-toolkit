# data-engineering-toolkit
A collection of scripts for common data engineering tasks.

**Project Purpose**

The Data Engineering Toolkit is a collection of reusable scripts that demonstrate fundamental data engineering tasks. It provides examples for Data Cleaning Tasks, Data Transformation Tasks and Data Loading Tasks. This project is designed to practice branching strategies, version control and collaboration workflows while building a hands-on data engineering toolkit.

**Documentation**
1. Data Cleaning: Automating basic data cleansing tasks, removing duplicates, trimming white spaces, standardizing column naming, handle missing values (drop, mean, median, mode).
   
2. Data Transformation: Applying transformations to Pandas DataFrames, Dropping irrelevant columns, Renaming columns, handling missing values for both numeric and non-numeric columns.

3. Data Loading: Auto-detect file format and convert to Parquet, Writing/Loading dataframe into different file formats (Parquet, CSV, JSON), Save CSV to DataFrame, and Save JSON to DataFrame


**Code Examples**

*Data Cleaning*

from data_cleaning_script import remove_duplicates, standardize_column_names

import pandas as pd

df = pd.DataFrame({
    "Student Name": ["Tom", "Jerry", "Tom"],
    "Age": [18, 20, 18]
})

df = remove_duplicates(df)
df = standardize_column_names(df)
print(df)


*Data Loading Example*

from data_loading_script import load_to_csv

import pandas as pd

df = pd.DataFrame({
    "Name": ["Tom", "Jerry"],
    "Score": [92, 87]
})

load_df_to_csv(df, "students.csv")


**Contribution Guide**

I followed the Gitflow branching strategy:

main → Branch for stable, production-ready code.

develop → Integration branch.

feature/branch-name → Branch for each script (e.g., feature/data-cleaning).


**Steps I followed to Contribute:**

Created repository on Github

Cloned the repository to my local directory

Created a develop branch

Created each feature branch: git checkout -b feature/feature-name

Add files to git

Committed changes frequently: git commit -m "Add new cleaning function"

Pushed each branch to the develop branch: git push origin feature/feature-name

Reviewed and checked for necessary changes

Opened a Pull Request to merge into develop

When it was all set, I merged the develop branch into main.


Note: This project is for learning and practice. Reviews are welcome, especially on scripts, code guidelines, optimizations, additional functions or documentation. Thank You!
