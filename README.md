
# Data_extraction with Python

## Overview

Generally, this is a Computer program-Tool in Python for automating the extraction of structured information such as financial data and dates from PDF documents-invoices, receipts, or reports. An efficient and scalable solution for batch processing of many PDF files while exporting the data information to a user-friendly Excel or CSV format. 


## Features


1)PDF Parsing:
    Utilizes libraries like PyPDF2 and pdfplumber to extract textual data from PDF documents.

2)Data Extraction with Regular Expressions:
Values: Identifies patterns like "Total USD" or "Gross Amount incl. VAT" using regular expressions to extract values in both USD and EUR.
Dates: Detects and parses dates in English and German formats, normalizing them to a consistent format.

3)Data Standardization:
Converts values into a common currency (e.g., USD to EUR).
Formats dates uniformly for easy analysis.

4)Multi-File Processing:
Processes multiple PDFs in a directory, extracting information efficiently through iteration.

5)Data Export:
Outputs data into structured formats:
    Excel: Includes a pivot table summarizing values by file and date.
    CSV: Provides a lightweight, tabular format for easy integration with other tools.


# How It Works!

## Task 1 :- Data Extraction

•	Utilizes a single function and two variables for streamlined data extraction.<br>
•   The keywords and PDF file names are stored in the variables keywords and pdf_files, respectively.<br>
•   Employs a list to store the extracted data for further processing.<br>
•   Iterates through PDF files in the directory using a for loop.<br>
•   Leverages the pdfplumber library to open and extract text from PDF files.<br>
•   A nested for loop searches for predefined keywords within the extracted text.<br>
•   It defines conditions based on the provided keywords.<br>
•   Searches for matching patterns in the text using regular expressions (re).<br>
NOTE: - The files and scripts should be placed under same directory<br>
Requirement: -<br>
    Python 3.6 or later<br>
Required libraries:<br>
    pdfplumber<br>
    re<br>

## Task 2: - Excel File Creation

Required import:<br>
    import os
    import sys
    from PyPDF2 import PdfReader
    import re
    import pandas as pd
    import dateparser<br>
Explanation:-<br>
    •	The program begins by searching a specified directory for PDF files..<br>
    •	Variables are created to store regex patterns, dates, currency conversion rates, and dictionaries for extracted data<br>
    •	The script uses multiple functions to achieve the desired output in a modular and structured way.<br>
    •	A function is used to locate and open PDF files. The text content of each PDF is extracted for further processing.<br>
    •	The extract_amount function:<br>
            Extracts amounts from the PDF text.<br>
            Converts currency values (e.g., from USD to EUR) for standardization.<br>
        The extract_date function:<br>
            Extracts and standardizes dates using the dateparser library to follow a consistent format.<br>
    •	The create_dataframe function:<br>
            Creates a table-like structure with headers: File Name, Date, and Value.<br>
            A loop and dictionaries are used to populate the data dynamically.<br>
    •	The standardized data is saved in both Excel and CSV formats.<br>
            The output files are stored in the same directory as the script.<br>

## Task 3 :- Generating CSV file

    The CSV includes headers, and use a semicolon (;) as the separator.

## Taks 4 :- Executable File
    'extract_invoice_data.exe' double click on the exe file to generate excel & csv file

## Task 5 :- Requirement file
    A requirements.txt file is provided to create the environment needed to run the code
