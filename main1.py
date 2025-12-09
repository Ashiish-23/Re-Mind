from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import datetime

class ToDoItem:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        
class ToDoItemWidget(BoxLayout):
    title = ObjectProperty(None)
    description = ObjectProperty(None)
    due_date = ObjectProperty(None)

    def __init__(self, todo_item, **kwargs):
        super().__init__(**kwargs)
        self.title.text = todo_item.title
        self.description.text = todo_item.description
        self.due_date.text = todo_item.due_date.strftime("%Y-%m-%d")
        
class ToDoList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data = []
        self.refresh_data()

    def refresh_data(self):
        self.data = [
            {"viewclass": "ToDoItemWidget", "height": 100, "todo_item": todo_item}
            for todo_item in MDApp.get_running_app().todo_items
        ]
        
        
class MainScreen(Screen):
    todo_list = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.todo_list = ToDoList()
        
        
class ToDoApp(MDApp):
    def build(self):
        self.todo_items = []
        self.theme_cls.primary_palette = "Blueviolet"
        return Builder.load_file("Lab.kv")

    def add_todo(self, title, description, due_date):
        todo_item = ToDoItem(title, description, due_date)
        self.todo_items.append(todo_item)
        self.root.ids.main_screen.todo_list.refresh_data()

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        self.root.ids.main_screen.ids.current_time.text = datetime.datetime.now().strftime("%H:%M:%S")
ToDoApp().run()        
        