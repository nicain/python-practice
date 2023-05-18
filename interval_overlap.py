class Interval:

  def __init__(self, start, end):
    self.start = start
    self.end = end

  def overlap(self, other):
    return (
      min(self.end, other.end) - 
      max(self.start, other.start)
    ) > 0