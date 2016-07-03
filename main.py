from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.listview import ListView, ListItemButton
#from kivy.factory import Factory
#from kivy.properties import ListProperty, StringProperty, ObjectProperty
# We'll probably need these later, when we want to modify their logic in the
# Python file.

class YpnApp(App):
    pass

class RootWidget(BoxLayout):
    def display_discounts_page(self):
        self.clear_widgets()
        self.add_widget(DiscountsPage())
        
    #todo: def display_calendar_page(self):
    #self.clear_widgets()
    #self.add_widget(CalendarPage())
    #something like that
    
    def display_articles_page(self):
        self.clear_widgets()
        self.add_widget(ArticlesPage())
        
class DiscountsPage(BoxLayout):
    pass

class ArticlesPage(BoxLayout):
    pass

# This is the code that actually runs the app.
if __name__ == '__main__':
    YpnApp().run()
