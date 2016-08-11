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
    # variable to contain a three-char slug denoting the last non-menu page
    # opened by user. Used by the Back button on the menu.
    last_page_open = "cal"
    # nts: this might be kind of weird with the discounts page if the menu
    # button isn't disabled while coupons are open. make sure there's no way
    # for users to "cheat" for multiple uses of coupons.

    def display_calendar_page(self):
        self.clear_widgets()
        self.add_widget(CalendarPage())
        self.last_page_open = "cal"

    def display_discounts_page(self):
        self.clear_widgets()
        self.add_widget(DiscountsPage())
        self.last_page_open = "dis"
        
    def display_articles_page(self):
        self.clear_widgets()
        self.add_widget(ArticlesPage())
        self.last_page_open = "art"
        
    def display_about_us_page(self):
        self.clear_widgets()
        self.add_widget(AboutUsPage())
        self.last_page_open = "abo"
    
    #def display_search_page(self):
    #    self.clear_widgets()
    #    self.add_widget(SearchPage())
    
    def display_menu_page(self):
        self.clear_widgets()
        self.add_widget(MenuPage())

    def display_last_page(self):
        # clumsy programming style. Python doesn't have switch statements; I
        # will neaten up this code in the way you're supposed to later, when I
        # don't have so many other things on my mind. Right now I just want it
        # to work and if it doesn't, I want to know this isn't the problem.
        if self.last_page_open == "cal":
            self.display_calendar_page()
        if self.last_page_open == "dis":
            self.display_discounts_page()
        if self.last_page_open == "art":
            self.display_articles_page()
        if self.last_page_open == "abo":
            self.display_about_us_page()
        
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
