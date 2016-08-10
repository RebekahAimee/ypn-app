# The MIT License (MIT)
# Copyright (c) <year> <copyright holders>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
    def display_calendar_page(self):
        self.clear_widgets()
        self.add_widget(CalendarPage())

    def display_discounts_page(self):
        self.clear_widgets()
        self.add_widget(DiscountsPage())
        
    def display_articles_page(self):
        self.clear_widgets()
        self.add_widget(ArticlesPage())
        
    def display_about_us_page(self):
        self.clear_widgets()
        self.add_widget(AboutUsPage())
    
    #def display_search_page(self):
    #    self.clear_widgets()
    #    self.add_widget(SearchPage())
    
    def display_menu_page(self):
        self.clear_widgets()
        self.add_widget(MenuPage())
        
class CalendarPage(BoxLayout):
    pass

class DiscountsPage(BoxLayout):
    pass

class ArticlesPage(BoxLayout):
    pass

class AboutUsPage(BoxLayout):
    pass

#class SearchPage(BoxLayout):
#    pass

class MenuPage(BoxLayout):
    pass

# This is the code that actually runs the app.
if __name__ == '__main__':
    YpnApp().run()
