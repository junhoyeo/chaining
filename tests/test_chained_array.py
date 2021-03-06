from chaining import ChainedArray


def test_representation():
    array = ChainedArray([1, 2, 3])
    assert str(array) == '<ChainedArray [1, 2, 3]>'


class TestProperties:
    def test_length(self):
        base_list = [1, 2, 3]
        array = ChainedArray(base_list)
        assert array.length == len(base_list)


class TestStaticMethods:
    def test_from(self):
        base_string = 'chain'
        array = ChainedArray._from(base_string)
        assert array.iterable == list(base_string)

    def test_is_chain_list(self):
        array = ChainedArray([1, 2, 3])
        for wrong_obj in [[], '', 1]:
            assert ChainedArray._is_chain_list(wrong_obj) == False
        assert ChainedArray._is_chain_list(array)


class TestInstanceMethods:
    first_array_original = [1, 2, 3]
    first_array = ChainedArray(first_array_original)

    second_array_original = [4, 5, 6]
    second_array = ChainedArray(second_array_original)

    def test_concat(self):
        concatenated_array = self.first_array.concat(self.second_array)
        assert concatenated_array.iterable == self.first_array_original + \
            self.second_array_original
        assert concatenated_array.iterable == [1, 2, 3, 4, 5, 6]

    def test_copy_within(self):
        array = ChainedArray(['a', 'b', 'c', 'd', 'e'])
        assert array.copy_within(0, 3, 4).iterable == ['d', 'b', 'c', 'd', 'e']
        assert array.copy_within(1, 3).iterable == ['d', 'd', 'e', 'd', 'e']

    def test_entries(self):
        iterator = self.first_array.entries()
        assert [item for item in iterator] == self.first_array_original

    def test_every(self):
        is_below = lambda item: item < 40

        assert self.first_array.every(is_below)
        assert self.second_array.every(is_below)

        array = ChainedArray([30, 40, 50])
        assert array.every(is_below) == False

    def test_fill(self):
        array = ChainedArray([1, 2, 3, 4])
        assert array.fill(0, 2, 4).iterable == [1, 2, 0, 0]
        assert array.fill(5, 1).iterable == [1, 5, 5, 5]
        assert array.fill(6).iterable == [6, 6, 6, 6]

    def test_filter(self):
        is_long = lambda word: len(word) > 6
        words = ChainedArray(
            ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'])

        filtered_words = words.filter(is_long)
        assert filtered_words.iterable == [
            'exuberant', 'destruction', 'present']

    def test_find(self):
        array = ChainedArray([5, 12, 8, 130, 44])
        is_above_ten = lambda number: number > 10

        assert array.find(is_above_ten) == 12

    def test_find_index(self):
        array = ChainedArray([5, 12, 8, 130, 44])
        is_large = lambda number: number > 13

        assert array.find_index(is_large) == 3

    def test_flat(self):
        first_array = ChainedArray([1, 2, [3, 4]])
        assert first_array.flat().iterable == [1, 2, 3, 4]

        second_array = ChainedArray([1, 2, [3, 4, [5, 6]]])
        assert second_array.flat().iterable == [1, 2, 3, 4, [5, 6]]

        third_array = ChainedArray([1, 2, [3, 4, [5, 6]]])
        assert third_array.flat(2).iterable == [1, 2, 3, 4, 5, 6]

    def test_flat_map(self):
        array = ChainedArray([1, 2, 3, 4])
        multiply = lambda item: [item * 2]
        multiply_only_one_level = lambda item: [[item * 2]]

        assert array.flat_map(multiply).iterable == [2, 4, 6, 8]
        assert array.flat_map(multiply_only_one_level).iterable == [
            [2], [4], [6], [8]]

    def test_for_each(self):
        result = []
        append_to_result = lambda item: result.append(item)

        self.first_array.for_each(append_to_result)
        assert result == self.first_array.iterable

    def test_includes(self):
        assert self.first_array.includes(1)
        assert not self.first_array.includes(1, 1)
        assert not self.first_array.includes(4)
        assert not self.first_array.includes('1')

    def test_index_of(self):
        assert self.first_array.index_of(1) == 0
        pass

    def test_join(self):
        pass

    def test_keys(self):
        pass

    def test_last_index_of(self):
        pass

    def test_map(self):
        multiply = lambda item: item * 2
        mapped_array = self.first_array.map(multiply)

        assert mapped_array.iterable == [
            multiply(item) for item in self.first_array_original]
        assert mapped_array.iterable == [2, 4, 6]

    def test_pop(self):
        pass

    def test_push(self):
        pass
