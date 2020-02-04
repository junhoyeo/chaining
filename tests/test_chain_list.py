from chaining import ChainList

def test_representation():
  array = ChainList([1, 2, 3])
  assert str(array) == '<ChainList [1, 2, 3]>'

class TestPoperties:
  def test_length(self):
    base_list = [1, 2, 3]
    array = ChainList(base_list)
    assert array.length == len(base_list)

class TestStaticMethods:
  def test_from(self):
    base_string = 'chain'
    array = ChainList._from(base_string)
    assert array.iterable == list(base_string)

  def test_is_chain_list(self):
    array = ChainList([1, 2, 3])
    for wrong_obj in [[], '', 1]:
      assert ChainList._is_chain_list(wrong_obj) == False
    assert ChainList._is_chain_list(array) == True

class TestInstanceMethods:
  first_array_original = [1, 2, 3]
  first_array = ChainList(first_array_original)

  second_array_original = [4, 5, 6]
  second_array = ChainList(second_array_original)

  def test_map(self):
    multiply = lambda item: item * 2
    mapped_array = self.first_array.map(multiply)
    assert mapped_array.iterable == [multiply(item) for item in self.first_array_original]
    assert mapped_array.iterable == [2, 4, 6]

  def test_concat(self):
    concatenated_array = self.first_array.concat(self.second_array)
    assert concatenated_array.iterable == self.first_array_original + self.second_array_original
    assert concatenated_array.iterable == [1, 2, 3, 4, 5, 6]
