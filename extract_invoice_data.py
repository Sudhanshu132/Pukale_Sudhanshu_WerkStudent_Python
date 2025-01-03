import os
import sys
from PyPDF2 import PdfReader
import re
import pandas as pd
import dateparser


# INPUT_PDF_PARENT_DIR = 'invoices'
INPUT_PDF_PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Constants
AMOUNT_PATTERN = r'(?:Total USD\s?\$(\d+[.,]?\d*)|Gross Amount incl. VAT\s?(\d+[.,]?\d*)\s?€)'
DATE_PATTERN = r'(Invoice date[:\s]*([A-Za-z]+ \d{1,2}, \d{4}))|(\d{1,2}\. [A-Za-zäöüßÄÖÜ]+ \d{4})'
USD_TO_EUR_RATE = 0.96
BASE_CURRENCY = '€'
DATE_FORMAT = '%Y-%m-%d'

pdf_amount_map = {}
pdf_date_map = {}

def pdf_files_path():
    '''
    Returns:
        List[str]: A list of PDF file paths.
    
    This function scans the provided directory, filters out PDF files,
    and returns a list of paths to those PDF files.
    '''
    global INPUT_PDF_PARENT_DIR
    if getattr(sys, 'frozen', False):
        INPUT_PDF_PARENT_DIR = os.path.dirname(sys.executable)
    files = os.listdir(INPUT_PDF_PARENT_DIR) # Get PDF files path under INPUT_PDF_PARENT_DIR
    pdf_files = [os.path.join(INPUT_PDF_PARENT_DIR, f) for f in files if f.lower().endswith('.pdf')]

    return pdf_files

def read_pdf(pdf_path):
    """
    Reads and extracts text from the first page of a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text content from the first page of the PDF.
    """
    with open(pdf_path, 'rb') as file:
        # PDF Reader object
        reader = PdfReader(pdf_path)

        # Extract text from the first page (index 0)
        first_page = reader.pages[0]
        text = first_page.extract_text()

        return text

def extract_amount(text, pdf_fname):
    """
    Extracts monetary amounts in USD or EUR from the given text.

    Args:
        text (str): PDF text content.
        pdf_fname (str): Name of the PDF file.

    Side Effects:
        Updates the global `pdf_amount_map` dictionary with extracted amounts,
        converting USD to EUR when applicable.
    """

    # Search for the EUR price in the text
    matches = re.findall(AMOUNT_PATTERN, text)

    for usd_match, eur_match in matches:
        if usd_match:  # If USD amount is found
            usd_amt = float(usd_match.replace(',', '.'))  # Convert to float
            eur_amt = usd_amt * USD_TO_EUR_RATE  # Convert USD to EUR

            pdf_amount_map[pdf_fname] = eur_amt
        
        if eur_match:  # If Euro amount is found
            eur_amt = float(eur_match.replace(',', '.'))  # Convert to float
            pdf_amount_map[pdf_fname] = eur_amt


def extract_date(text, pdf_fname):
    """
    Extracts invoice dates in English or German formats from the text.

    Args:
        text (str): PDF text content.
        pdf_fname (str): Name of the PDF file.

    Side Effects:
        Updates the global `pdf_date_map` dictionary with standardized dates in `YYYY-MM-DD` format.
    """

    # Search for DATE_PATTERN
    matches = re.findall(DATE_PATTERN, text)
    
    for match in matches:
        _, english_date, german_date = match   #tuple unpacking
        
        # If an English date is found, parse it
        if english_date:
            try:
                # Parse English date with dateparser
                parsed_date = dateparser.parse(english_date.strip())
                if parsed_date:
                    pdf_date_map[pdf_fname] = parsed_date.strftime(DATE_FORMAT)
            except Exception as e:
                print(f"Error parsing English date: {e}")

        # If a German date is found, parse it
        if german_date:
            try:
                # Parse German date with dateparser (specifying German language)
                parsed_date = dateparser.parse(german_date.strip())
                if parsed_date:
                    pdf_date_map[pdf_fname] = parsed_date.strftime(DATE_FORMAT)
            except Exception as e:
                print(f"Error parsing German date: {e}")

def create_dataframe():
    """
    Combines the extracted data into a pandas DataFrame.

    Returns:
        pd.DataFrame: DataFrame containing file names, dates, and values.
    """
    data = {
        'File Name': list(pdf_amount_map.keys()),
        'Date': [pdf_date_map[file] for file in pdf_date_map.keys()],
        'Value': list(pdf_amount_map.values())
    }

    return pd.DataFrame(data)

def save_to_excel(df):
    """
    Saves the extracted data to an Excel file with two sheets:
    - Raw data(Sheet 1).
    - Pivot table summarizing values by date and file name.(Sheet 2)

    Args:
        df (pd.DataFrame): DataFrame containing the extracted data.
    
    return:
        creates excel file with sheet 1 and sheet 2
    """
    # Optional: To add EURO symbol
    # df['Value'] = df['Value'].apply(lambda x: f'{x:.2f}€')

    # Step 2: Create a Pivot Table for Sheet 2
    pivot_df = pd.pivot_table(df, values='Value', index='Date', columns='File Name', aggfunc='sum', fill_value=0)

    # Step 3: Write to Excel
    with pd.ExcelWriter('invoices.xlsx', engine='openpyxl') as writer:
        # Write the DataFrame to the first sheet
        df.to_excel(writer, sheet_name = 'Sheet 1', index=False)
        # Write the pivot table to the second sheet
        pivot_df.to_excel(writer, sheet_name = 'Sheet 2')
    
    print("Excel file 'invoices.xlsx' created successfully.")

def save_to_csv(df):
    """
    Saves the extracted data to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame containing the extracted data.
"""
    df.to_csv('invoices.csv', sep=';', index=False)
    print("CSV file 'invoices.csv' created successfully.")


### Driver code

files = pdf_files_path()
if not files:
    print(f"Error: No PDF files found at {INPUT_PDF_PARENT_DIR}. \nPlease place required files to run the program.")
    sys.exit(1)

for pdf_fpath in files:

    pdf_fname = os.path.basename(pdf_fpath).replace('.pdf','')
    text = read_pdf(pdf_fpath)  # Read the text from each PDF file
    
    # 1. Data extraction 
    extract_amount(text, pdf_fname)
    extract_date(text, pdf_fname)

if pdf_amount_map and pdf_date_map:
    print("Data extracted succefully.")
else:
    print("Error occured while extracting data.")
    sys.exit(1)

# 2. Excel File Creation
df = create_dataframe()
save_to_excel(df)

# 3. CSV File Creation
save_to_csv(df)

input = ('Program finished.Press enter to exit')