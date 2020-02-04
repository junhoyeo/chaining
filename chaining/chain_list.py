class ChainList:
  iterable = []
  length = 0

  def __init__(self, array):
    self.iterable = array
    self.length = len(array)

  def __repr__(self):
    return f'<ChainList {str(self.iterable)}>'

  @staticmethod
  def _from(array_like):
    return ChainList(list(array_like))

  def map(self, callback):
    return ChainList([
      callback(item)
      for item in self.iterable
    ])

  def concat(self, array_like):
    is_chain_list = type(array_like) == ChainList
    array = array_like.iterable if is_chain_list else list(array_like)
    return ChainList(self.iterable + array)
