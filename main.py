from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.textinput import TextInput


class Home(Screen):
    pass

class Exp_Page(Screen):
    def type_click(self,value):
        self.ids.type_exp.text = value

    def add_expence(self):
        amount = self.ids.amt_inp.text
        type_amt = self.ids.type_exp.text
        note = self.ids.note_inp.text
        print("amt = ",amount,"\ntype = ",type_amt,"\nnote = ",note)
        self.ids.amt_inp.text = ""
        self.ids.type_exp.text= "Type"
        self.ids.note_inp.text = ""


class Inc_Page(Screen):
    def add_income(self):
        amount = self.ids.amt_inp.text
        note = self.ids.note_inp.text
        print("amt = ",amount,"\nnote = ",note)
        self.ids.amt_inp.text = ""
        self.ids.note_inp.text = ""

class Display_Page(Screen):
    pass

class Delete_Page(Screen):
    def type_click(self, value):
        self.ids.type_del.text= value
    def delete_rec(self):
        iden = self.ids.del_id.text
        del_type = self.ids.type_del.text
        print("type = ",del_type,"\nid = ",iden)
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