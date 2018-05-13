class Director(object):

  def __init__(self, screen):
    self.current = screen

  def is_running(self):
    return self.current.running

  def update(self):
    # Check if the scene was changed
    if(self.current.changed_screen):
      self.current = self.current.next_screen
    self.current.run()
