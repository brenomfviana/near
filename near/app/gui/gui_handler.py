from tkinter import *
from gui.login import Login

class GUIHandler(object):

  def __init__(self):
    self.root = Tk()

  def run(self):
    screen = Login(self.root)
    screen.run()
