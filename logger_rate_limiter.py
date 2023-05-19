class Logger:

  def __init__(self):
    self.data = {}
    
  def shouldPrintMessage(self, timestamp, message):
    if message in self.data:
      if timestamp < self.data[message] + 10:
        return False
      else:
        self.data[message] = timestamp
        return True
    else:
      self.data[message] = timestamp
      return True