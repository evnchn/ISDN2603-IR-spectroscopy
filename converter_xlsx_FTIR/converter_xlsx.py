import pandas as pd

def xlsx_to_csv(filename):
    # Load the Excel file
    xls = pd.ExcelFile(filename)

    # Iterate through each sheet
    for sheet_name in xls.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(filename, sheet_name=sheet_name)

        # Save the DataFrame as a CSV file
        csv_filename = f"{filename}-{sheet_name}.csv"
        df.to_csv(csv_filename, index=False)
        print(f"Saved {csv_filename}")

# Usage example
xlsx_to_csv("group1.xlsx")
xlsx_to_csv("group2.xlsx")