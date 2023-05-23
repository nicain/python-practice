"""
Design a logger system that receives a 
stream of messages along with their 
timestamps. Each unique message should only 
be printed at most every 10 seconds (i.e. a 
message printed at timestamp t will prevent 
other identical messages from being printed 
until timestamp t + 10).

All messages will come in chronological 
order. Several messages may arrive at the 
same timestamp.

Implement the Logger class:

Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, 
  string message) Returns true if the 
  message should be printed in the given 
  timestamp, otherwise returns false.
"""

source_url = (
  'https://leetcode.com/problems/'
  'logger-rate-limiter'
)

title = (
  'Logger Rate Limiter'
)


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