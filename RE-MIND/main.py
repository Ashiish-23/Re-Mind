# Dependencies
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers.datepicker import MDDatePicker

from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox

from datetime import datetime

import taskmanager as TM

#Dialog box class
class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

    #function for date dialog picker
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    pass

    def __init__(self,pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk
    #mark the task as complete or incomplete
    def mark(self, check, the_list_item):
        if check.active == True:
            the_list_item.text = '[s]'+the_list_item.text+'[/s]'
            TM.task_complete(self.pk)

        else:
            the_list_item.text = TM.task_incomplete(self.pk)

    def delete_item(self, the_list_item):
        TM.pop_task(self.pk)
        self.parent.remove_widget(the_list_item)
        

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    pass

# Main App class
class ReMindApp(MDApp):
    task_list_dialog = None
    tasks = []
    def build(self):
        # Setting theme to my favorite theme
        self.theme_cls.primary_palette = "Orange"
        
    # Showing the task dialog to add tasks 
    def show_task_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog = MDDialog(
                title="Create Task",
                type="custom",
                content_cls=DialogContent(),
            )

        self.task_list_dialog.open()

    #Function performs tasks when the application starts
    def on_start(self):
        load_bool = TM.list_store()
        if load_bool:
            stored_task_items = TM.load_tasks()
            print("True")
            print(type(stored_task_items))
            print(stored_task_items)

            for i in range(len(stored_task_items)):
                if stored_task_items[i][3] == True:
                    add_task = ListItemWithCheckbox(
                        pk=stored_task_items[i][0],
                        text='[s]' + str(stored_task_items[i][1]) + '[/s]', 
                    )
                    add_task.ids.check.active = True
                else:
                    add_task = ListItemWithCheckbox(
                        pk=stored_task_items[i][0],
                        text=str(stored_task_items[i][1]),  
                        secondary_text=stored_task_items[i][2]
                    )
                self.root.ids.container.add_widget(add_task)

                
        else:
            pass

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

    #function for add_task on save button
    def add_task(self, task, task_date):

        #Add Tasks to json
        TM.add_task(task.text,task_date)

        #Load Tasks items
        task_items = TM.get_tasks()

        # return the created task details and create a list item
        self.root.ids['container'].add_widget(ListItemWithCheckbox(pk=task_items[0],text=task_items[1], secondary_text=task_items[2]))
        task.text = ''

if __name__ == '__main__':
    app = ReMindApp()
    app.run()