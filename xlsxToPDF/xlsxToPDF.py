import win32com.client
from pywintypes import com_error
import os
from pathlib import Path
import argparse

def xlsxToPDF(inp_filename,out_filename,excel_pages):
    # Input and Output filenames
    XLSX_FILENAME = inp_filename
    PDF_FILENAME = out_filename.split(".")[0]+ ".pdf"

    # Current directory path
    dir_path = os.path.dirname(os.path.realpath('__file__'))

    # Path to original excel file
    EXCEL_PATH = os.path.join(dir_path,XLSX_FILENAME) 

    # PDF path when saving
    PDF_PATH = os.path.join(dir_path,PDF_FILENAME)

    #Specify the number of pages in ur excelsheet
    EXCEL_PAGES = excel_pages

    #Setting Excel Application
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False

    try:
        # Open XLSX file
        wb = excel.Workbooks.Open(EXCEL_PATH)
    except:
        print("{} file not found in the directory {}".format(XLSX_FILENAME,dir_path))
        print("Exiting program....")
        exit()

    try:
        input("Press Enter to start conversion from XLSX to PDF: ")

        # lists out the sheets available in ur Excel sheet
        ws_index_list = [i for i in range(1,EXCEL_PAGES+1)]
        wb.WorkSheets(ws_index_list).Select()

        # Save
        wb.ActiveSheet.ExportAsFixedFormat(0, PDF_PATH)

    except com_error as e:
        print('\nConversion failed...')
        print(e)
        exit()

    else:
        print('\nConversion Succeeded...')
        print("{} created at path : {}".format(PDF_FILENAME,dir_path))
        

    finally:
        wb.Close()
        excel.Quit()

    exit()



def main():
    #parsing commadline args
    parser = argparse.ArgumentParser(description="Convert any XLSX file to PDF file")

    #Input filename
    parser.add_argument('-inp', type = str, help = "Enter the XLSX filename as input")
    
    #Output filename
    parser.add_argument('-out', type = str, help = "Enter the PDF filename as output")

    #No of Pages in the XLSX file
    parser.add_argument('-pg', type = int, help = "Enter the number of pages in the XLSX file")

    try:
        args = parser.parse_args()

        if((args.inp is not None) and (args.pg is not None)):
            if (args.out is not None):
                xlsxToPDF(args.inp,args.out,args.pg)
            else:
                args.out = args.inp 
                xlsxToPDF(args.inp,args.out,args.pg)

    except Exception as e:
        print("Error occured")
        print(e)
        exit()

if __name__ == '__main__':
    main()
