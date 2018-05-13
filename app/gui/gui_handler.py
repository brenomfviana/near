from tkinter import *
from gui.director import Director
from gui.login import Login

class GUIHandler(object):

  def __init__(self):
    self.root = Tk()
    self.director = Director(Login(self.root))

  def run(self):
    while(self.director.is_running()):
      self.director.update()
