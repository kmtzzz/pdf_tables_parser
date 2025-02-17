import os

import pandas as pd

import pdfplumber

# put file name to be processed without extension
file_name = 'order_types'

# build absolute path to .pdf file
pdf_file = os.path.abspath(f'{file_name}.pdf')

# read and process PDF
try:
    pd_df = pd.DataFrame()
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            p = pd.DataFrame(page.extract_table())
            pd_df = pd.concat([pd_df, p])
    
    # create file with same name and .csv extension in cyrilic encoding
    pd_df.to_csv(f'{file_name}.csv',encoding='utf-8-sig', sep=';')

    # prompt processing is finished
    print(f'File {file_name}.csv is created')

except FileNotFoundError:
    print(f'File with path {pdf_file} was not found')


