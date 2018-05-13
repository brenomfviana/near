from tkinter import *

class Chat(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.window = master
    self.window.protocol('WM_DELETE_WINDOW', self.quit)
    self.running = True
    self.changed_screen = False
    self.next_screen = None
    # Init components
    self.init_components()

  def init_components(self):
    # Title
    self.window.title("Near - Chat")
    self.window.resizable(width=False, height=False)
    self.configure(background="white")
    # Public chat
    label_t = Label(self, text="Public chat", width=10, background="white")
    label_t.grid(row=0, column=0, padx=(5, 5), pady=(7, 7), sticky=W)
    # Logoff
    label_l = Button(self, text="Logoff", width=10, command=self.logoff)
    label_l.grid(row=0, column=9, padx=(5, 5), pady=(7, 7), sticky=E)
    # Messages
    messages = Text(self, width=62, height=24, background="white")
    messages.grid(row=1, column=0, columnspan=10, sticky=W+E)
    messages.config(state=DISABLED)
    # Message
    message = Entry(self, width=20, background="white")
    message.grid(row=2, column=0, columnspan=8, padx=(5, 0), pady=(7, 7), sticky=W+E)
    # Send
    send = Button(self, text="Send", width=10, command=self.send)
    send.grid(row=2, column=9, padx=(5, 5), pady=(7, 7), sticky=E)
    # Centralize window
    self.center()

  def send(self):
    pass

  def logoff(self):
    self.changed_screen = True
    import gui.login
    self.next_screen = gui.login.Login(self.window)
    self.grid_forget()

  def quit(self):
    self.next_screen = None
    self.running = False
    self.window.destroy()

  def center(self):
    self.window.update_idletasks()
    w = self.window.winfo_screenwidth()
    h = self.window.winfo_screenheight()
    size = tuple(int(_) for _ in self.window.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    self.window.geometry("%dx%d+%d+%d" % (size + (x, y)))

  def run(self):
    if self.running:
      self.window.mainloop()
