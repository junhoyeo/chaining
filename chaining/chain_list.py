class ChainList:
  iterable = []

  def __init__(self, array):
    self.iterable = array

  def __repr__(self):
    return f'<ChainList {str(self.iterable)}>'
