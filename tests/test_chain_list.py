from chaining import ChainList

def test_representation():
  array = ChainList([1, 2, 3])
  assert str(array) == '<ChainList [1, 2, 3]>'

def test_properties():
  base_list = [1, 2, 3]
  array = ChainList(base_list)
  assert array.length == len(base_list)

def test_static_methods():
  base_string = 'chain'
  array = ChainList._from(base_string)
  assert array.iterable == list(base_string)

  for wrong_obj in [[], '', 1]:
    assert ChainList._is_chain_list(wrong_obj) == False
  assert ChainList._is_chain_list(array) == True

def test_instance_methods():
  first_array_original = [1, 2, 3]
  first_array = ChainList(first_array_original)

  second_array_original = [4, 5, 6]
  second_array = ChainList(second_array_original)

  multiply = lambda item: item * 2
  mapped_array = first_array.map(multiply)
  assert mapped_array.iterable == [multiply(item) for item in first_array_original]
  assert mapped_array.iterable == [2, 4, 6]

  concatenated_array = first_array.concat(second_array)
  assert concatenated_array.iterable == first_array_original + second_array_original
  assert concatenated_array.iterable == [1, 2, 3, 4, 5, 6]
