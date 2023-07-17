import pandas as pd

def find_empty_cell_index(row):
    """
    Finds the index of the column of the first cell in the row that is empty.

    Args:
        row: A Pandas Series object representing a row in an Excel file.

    Returns:
        The index of the column of the first empty cell in the row, or None if there are no empty cells in the row.
    """

    for i in range(len(row)):
        if row[i] == '':
            return i

    return None

def isolate_headers(row):
    """
    Isolates the headers from a row of a Pandas DataFrame.

    Args:
        row: A Pandas Series object representing a row in a Pandas DataFrame.

    Returns:
        A list of the headers in the row.
    """

    headers = []
    for i in range(len(row)):
        if row[i] != '':
            headers.append(row[i])

    return headers

if __name__ == '__main__':
    # Open the Excel file in read mode

    # Create a Pandas DataFrame from the Excel file
        df = pd.read_excel('tracker.xlsx')

        # Set the row variable to the first row of the DataFrame
        row = df.iloc[1]

        # Print the index of the first empty cell in the row
        print(isolate_headers(row))#find_empty_cell_index(row))
