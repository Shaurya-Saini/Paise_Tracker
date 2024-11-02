from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
import gspread
from google.oauth2.service_account import Credentials
from datetime import date,datetime,timedelta
from kivy.uix.label import Label
today = date.today().strftime('%Y-%m-%d')
scope = {
    "https://www.googleapis.com/auth/spreadsheets"
}
creds = Credentials.from_service_account_file("credentials.json",scopes = scope)
client = gspread.authorize(creds)

sheet_id = "1dPBI4HX54y_Uu45pZuxUs_e6_dqFOX3Q7rZSxV7m2NY"
workbook = client.open_by_key(sheet_id)

def check_week(date_str):
    input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week <= input_date <= end_of_week

def check_month(date_str):
    input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.today().date()
    start_of_month = today.replace(day=1)
    if today.month == 12:
        end_of_month = today.replace(month=1, year=today.year + 1, day=1) - timedelta(days=1)
    else:
        end_of_month = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
    return start_of_month <= input_date <= end_of_month

class Home(Screen):
    pass

class Exp_Page(Screen):
    def type_click(self,value):
        self.ids.type_exp.text = value

    def add_expence(self):
        exp_sheet = workbook.worksheet("Expences list")
        filled_rows = len(exp_sheet.get_all_values())
        amount = self.ids.amt_inp.text
        type_amt = self.ids.type_exp.text
        note = self.ids.note_inp.text
        exp_sheet.update_cell(filled_rows+1,1,today)
        exp_sheet.update_cell(filled_rows+1,2,amount)
        exp_sheet.update_cell(filled_rows+1,3,type_amt)
        exp_sheet.update_cell(filled_rows+1,4,note)
        self.ids.amt_inp.text = ""
        self.ids.type_exp.text= "Type"
        self.ids.note_inp.text = ""


class Inc_Page(Screen):
    def add_income(self):
        inc_sheet = workbook.worksheet("Income list")
        filled_rows = len(inc_sheet.get_all_values())
        amount = self.ids.amt_inp.text
        note = self.ids.note_inp.text
        inc_sheet.update_cell(filled_rows+1,1,today)
        inc_sheet.update_cell(filled_rows+1,2,amount)
        inc_sheet.update_cell(filled_rows+1,3,note)
        self.ids.amt_inp.text = ""
        self.ids.note_inp.text = ""

class Display_Page(Screen):
    def filter_records(self):
        self.on_pre_enter()

    def on_pre_enter(self):
        record_type = self.ids.record_spinner.text
        expense_type = self.ids.type_spinner.text
        date_filter = self.ids.date_spinner.text
        if (record_type=="Expense"):
            using = workbook.worksheet("Expences list")
        else:
            using = workbook.worksheet("Income list")
        data = using.get_all_values()[1:]
        self.ids.display_grid.clear_widgets()
        row_id = 1
        for record in data:
            if (record_type=="Expense" and expense_type!="All" ):
                if (record[2]!=expense_type):
                    continue
            if (date_filter=="Today"):
                if (record[0]!=today):
                    continue
            elif (date_filter=="This Week"):
                if (check_week(record[0])!=True):
                    continue
            elif (date_filter=="This Month"):
                if (check_month(record[0])!=True):
                    continue
            self.ids.display_grid.add_widget(Label(text=str(row_id), font_size="18dp"))
            self.ids.display_grid.add_widget(Label(text=record[0], font_size="18dp"))
            self.ids.display_grid.add_widget(Label(text=record[1], font_size="18dp"))
            self.ids.display_grid.add_widget(Label(text=record[2], font_size="18dp"))
            if len(record) > 3:
                self.ids.display_grid.add_widget(Label(text=record[3], font_size="18dp")) 
            else:
                self.ids.display_grid.add_widget(Label(text="N/A", font_size="18dp"))
            row_id += 1



class Delete_Page(Screen):
    def type_click(self, value):
        self.ids.type_del.text= value
    def delete_rec(self):
        exp_sheet = workbook.worksheet("Expences list")
        inc_sheet = workbook.worksheet("Income list")
        iden = int(self.ids.del_id.text)
        iden+=1
        del_type = self.ids.type_del.text
        
        if (del_type=="Expence"):
            using = exp_sheet
            using.update_cell(iden,1,"")
            using.update_cell(iden,2,"")
            using.update_cell(iden,3,"")
            using.update_cell(iden,4,"")
        else:
            using = inc_sheet
            using.update_cell(iden,1,"")
            using.update_cell(iden,2,"")
            using.update_cell(iden,3,"")
        
        all_rows = using.get_all_values()
        non_empty_rows = [row for row in all_rows if any(cell.strip() for cell in row)]
        using.clear()
        if non_empty_rows:
            using.update(f'A1:D{len(non_empty_rows)}', non_empty_rows)
        self.ids.del_id.text = ""
        self.ids.type_del.text = "Type"

class Rec_Page(Screen):
    pass

class WinMan(ScreenManager):
    pass

kv = Builder.load_file('application.kv')

class TrackerApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    TrackerApp().run()