import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.properties import NumericProperty

import bullsandcowslogic

class BullsAndCows(RelativeLayout):
	answer = NumericProperty(0)

	def __init__(self, **kwargs):
		super(BullsAndCows, self).__init__(**kwargs)
		self.answer = bullsandcowslogic.generate_answer()

	def button_pressed(self):
		values = self.ids.values()
		textinput = values[0].__self__
		widget = values[1].__self__
		widget.button_pressed(textinput.text)
		textinput.text = ""

class BullsAndCowsMainWidget(GridLayout):
	tries = NumericProperty(0)
	def __init__(self, **kwargs):
		super(BullsAndCowsMainWidget,self).__init__(**kwargs)

	def button_pressed(self, textinput):
		self.tries = self.tries + 1
		bulls = bullsandcowslogic.calculate_bulls(self.parent.answer,int(textinput))
		cows = bullsandcowslogic.calculate_cows(self.parent.answer,int(textinput))
		result = str(bulls) + " bulls and " + str(cows) + " cows" 
		self.add_widget(Label(text=str(self.tries)) )
		self.add_widget(Label(text=textinput ))
		self.add_widget(Label(text=result))
		self.pos_hint = ({'x':0, 'center_y':0.7 + 0.025*(1-self.tries)})
		self.size_hint = (1,0.05 * self.tries )




class BullsAndCowsApp(App):
	def build(self):
		return BullsAndCows()


if __name__ == '__main__':
	BullsAndCowsApp().run()
