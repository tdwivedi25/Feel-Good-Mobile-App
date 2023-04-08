from kivy.app import App
from kivy.lang import Builder # connects python to kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior 
import csv,glob, random
from datetime import datetime
from pathlib import Path

Builder.load_file('design.kv')

class LoginScreen(Screen):
   def sign_up(self):
      self.manager.current = "sign_up_screen"
   def login(self, uname, pword):
      with open(r"C:\Users\denali\Python_Basics\Feel-Good Mobile App\users.csv" ) as file:
         users = csv.reader(file)
         for lines in users:
            if uname and pword in lines:
               self.manager.current = "login_screen_success" 
            else:
               self.ids.login_wrong.text = "Wrong username or password"

class RootWidget(ScreenManager):
   pass

class SignUpScreen(Screen):
   def add_user(self, uname, pword):
      with open(r"C:\Users\denali\Python_Basics\Feel-Good Mobile App\users.csv",'a') as file:
         users=csv.writer(file)
         list1=[uname, pword, datetime.now().strftime("%Y-%m-%d %H-%M-%S")]
         users.writerow(list1)
      self.manager.current="sign_up_screen_success"

class SignUpScreenSuccess(Screen):
   def go_to_login(self):
      self.manager.transition.direction = "right"
      self.manager.current="login_screen"

class LoginScreenSuccess(Screen):
   def log_out(self):
      self.manager.transition.direction = "right"
      self.manager.current = "login_screen"
   
   def get_quote(self,feel):
      feel = feel.lower()
      available_feelings= glob.glob("quotes/*txt")

      available_feelings = [Path(filename).stem for filename in 
      available_feelings]
      
      if feel in available_feelings:
         with open (f"quotes/{feel}.txt") as file:
            quotes=file.readlines()
            self.ids.quote.text=random.choice(quotes)
      else: 
            self.ids.quote.text = "Try another feeling"
   
class ImageButton(ButtonBehavior, HoverBehavior, Image ):
   pass

class MainApp(App):
   def build(self):
      return RootWidget()

if __name__=="__main__":
   MainApp().run()