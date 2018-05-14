from tkinter import *
from tkinter import ttk

from domain.user import User
from gui.chat import Chat

class Login(Frame):

  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.root = master
    self.grid()
    self.window = master
    self.window.protocol('WM_DELETE_WINDOW', self.quit)
    self.running = True
    self.changed_screen = False
    self.next_screen = None
    # Init components
    self.init_components()

  def init_components(self):
    self.root.bind('<Return>', self.login)
    # Title
    self.window.title("Near - Login")
    self.window.resizable(width=False, height=False)
    self.configure(background="white")
    # Image logo
    logo = PhotoImage(file="assets/near.png")
    label = Label(self)
    label.image = logo
    label.configure(image=logo, background="white")
    label.grid(row=0, column=0, columnspan=4, padx=(100, 100), pady=(20, 20),
      sticky=W+E)
    # Server Address
    label_sa = Label(self, text="Server Address:", background="white")
    label_sa.grid(row=1, column=1)
    server_address = Entry(self, width=20, background="white")
    server_address.grid(row=1, column=2, pady=(5, 5), sticky=W+E)
    # User name
    label_un = Label(self, text="Username:", background="white")
    label_un.grid(row=2, column=1)
    self.username = Entry(self, width=20, background="white")
    self.username.grid(row=2, column=2, pady=(5, 5), sticky=W+E)
    # Language
    label_un = Label(self, text="Language:", background="white")
    label_un.grid(row=3, column=1)
    self.language = ttk.Combobox(self, width=20, background="white")
    self.language['values'] = ('English', 'Português Brasileiro', 'Français', 'Español', 'Italiano', 'Deutsch', 'Nederlands')
    self.language.grid(row=3, column=2, pady=(5, 10), sticky=W+E)
    # Login
    button_l = Button(self, text="Confirm", width=10, command=self.login)
    button_l.grid(row=4, column=0, columnspan=4, padx=(100, 100), pady=(5, 0))
    # Quit
    button_q = Button(self, text="Quit", width=10, command=self.quit)
    button_q.grid(row=5, column=0, columnspan=4, padx=(100, 100), pady=(5, 10))
    # Centralize window
    self.center()

  def login(self, event=NONE):
    user = User(self.username.get(), self.language.get())
    self.changed_screen = True
    self.next_screen = Chat(user, self.window)
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
