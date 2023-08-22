import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

def get_sales_data():
    """
    Gets sales data input from the user
    """
    print('Please enter the sales data from the last market.')
    print('Data should be six numbers, seperated by commas')
    print('Example, 10, 20, 30, 40, 60')

    data_str = input('Enter your data here: ')

    sales_data = data_str.split(',')
    validate_data(sales_data)


def validate_data(values):
    """
    Inside the try, converts all the string values into integers.
    Raise a ValueError if strings cannot be converted into a int,
    or if there are not exactly 6 values
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f'Exaclty 6 values required, you provided {len(values)}'
            )
    except ValueError as e:
        print(f'Inavlid data: {e}, please try again\n')


get_sales_data()