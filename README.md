
# WerkStudent_Python

## Overview

This repository contains the interview task for the WerkStudent position in Python. The goal is to collect data from three sample invoices, create an Excel file with two sheets, and generate a CSV file. Additionally, an executable file should be provided to run the code.

## Task Details

1. **Data Extraction**:
    - Extract specific values from three sample invoices.
    - For Sample 1, extract the value shown in the provided image.
    - <img width="289" alt="image" src="https://github.com/user-attachments/assets/0cf000ff-c305-4ffe-beb4-1c02a04d06b6" />
    - For Samples 2, extract the value shown in the provided image.
    - <img width="497" alt="image" src="https://github.com/user-attachments/assets/ea6eb368-604d-4dd4-9235-fbc8ec36d275" />

2. **Excel File Creation**:
    - Create an Excel file with two sheets:
        - **Sheet 1**: Contains three columns - File Name, Date (scraped from the document), and Value.
        - **Sheet 2**: Contains a pivot table with the date and value sum, and also by document name.

3. **CSV File Creation**:
    - Create a CSV file with all the data, including headers, and use a semicolon (;) as the separator.

4. **Executable File**:
    - Provide an executable file (.exe) that can run the code if the files are in the same folder.

5. **Branch Creation**:
    - Create a branch in this repository named `LastName_FirstName` (e.g., `Shovon_Golam`).
    - Upload your code to this branch. No need to submit a pull request; the branch will be checked directly.

6. **Documentation**:
    - Include an explanation in the README file that a non-technical person can understand.
    - Ensure the code is documented so that a technical person can understand it.

7. **Problem Reporting**:
    - If you face any problems or find it impossible to complete a task, document the issue in the README file of your branch. Explain what the problem was and why you were unable to complete it.


## How It Works

1. **Data Extraction**:
    - The script reads the sample invoices and extracts the required values.
    - The extracted data is stored in variables for further processing.

2. **Excel File Creation**:
    - The script creates an Excel file with two sheets.
    - Sheet 1 contains the file name, extracted data, and value.
    - Sheet 2 contains a pivot table summarizing the data by date and document name.

3. **CSV File Creation**:
    - The script generates a CSV file with the extracted data, including headers, and uses a semicolon as the separator.

4. **Executable File**:
    - An executable file is provided to run the entire code. Ensure the sample invoices are in the same folder as the executable file.

5. **Requirements File**:
    -A requirements.txt file is included to create the environment needed to run the code

## Running the Code

1. Place the sample invoices in the same folder as the executable file.
2. Run the executable file to execute the code and generate the Excel and CSV files.


## Documentation

- The README file contains a non-technical explanation of the code.
- The code is documented with comments to help technical users understand its functionality.

## Problem Reporting

- If you face any problems or find it impossible to complete a task, document the issue in the README file of your branch. Explain what the problem was and why you were unable to complete it.

## Timeline

- The time limit for this task is 9 January 2025. 


## Solution ------------------------------------------


## Task 1 :- Data Extraction

•	Utilizes a single function and two variables for streamlined data extraction.
•   The keywords and PDF file names are stored in the variables keywords and pdf_files, respectively.
•   Employs a list to store the extracted data for further processing.
•   Iterates through PDF files in the directory using a for loop.
•   Leverages the pdfplumber library to open and extract text from PDF files.
•   A nested for loop searches for predefined keywords within the extracted text.
•   It defines conditions based on the provided keywords.
•   Searches for matching patterns in the text using regular expressions (re). If a match is found, it
NOTE: - The files and scripts should be placed under same directory
Requirement: -
    Python 3.6 or later
Required libraries:
    pdfplumber
    re

## Task 2: - Excel File Creation

Required import:
    import os
    import sys
    from PyPDF2 import PdfReader
    import re
    import pandas as pd
    import dateparser
Explanation:-
    •	The program begins by searching a specified directory for PDF files..
    •	Variables are created to store regex patterns, dates, currency conversion rates, and dictionaries for extracted data
    •	The script uses multiple functions to achieve the desired output in a modular and structured way.
    •	A function is used to locate and open PDF files. The text content of each PDF is extracted for further processing.
    •	The extract_amount function:
        •    Extracts amounts from the PDF text.
        •    Converts currency values (e.g., from USD to EUR) for standardization.
        The extract_date function:
        •    Extracts and standardizes dates using the dateparser library to follow a consistent format.
    •	The create_dataframe function:
        •    Creates a table-like structure with headers: File Name, Date, and Value.
        •    A loop and dictionaries are used to populate the data dynamically.
    •	The standardized data is saved in both Excel and CSV formats.
        •The output files are stored in the same directory as the script.

## Task 3 :- Generating CSV file

    The CSV includes headers, and use a semicolon (;) as the separator.

## Taks 4 :- Executable File
    'extract_invoice_data.exe' double click on the exe file to generate excel & csv file

## Task 5 :- Requirement file
    A requirements.txt file is provided to create the environment needed to run the code