import gspread
from google.oauth2.service_account import Credentials

scope = {
    "https://www.googleapis.com/auth/spreadsheets"
}
creds = Credentials.from_service_account_file("credentials.json",scopes = scope)
client = gspread.authorize(creds)

sheet_id = "1dPBI4HX54y_Uu45pZuxUs_e6_dqFOX3Q7rZSxV7m2NY"
# in the link after the \d befor the edit
workbook = client.open_by_key(sheet_id)

values_list = workbook.sheet1.row_values(1)
print(values_list)