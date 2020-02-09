def callback_wrapper(callback, item, index, array, param_length):
    if param_length == 1:
        return callback(item)
    elif param_length == 2:
        return callback(item, index)
    return callback(item, index, array)


def _flatten(array, depth):
    result = []
    for item in array:
        item_type = type(item)
        if item_type in [tuple, list]:
            if depth:
                for element in _flatten(item, depth - 1):
                    result.append(element)
            else:
                result.append(item)
        else:
            result.append(item)
    return result


class ChainedArray:
    iterable = []

    def __init__(self, array):
        self.iterable = array

    def __repr__(self):
        return f'<ChainedArray {str(self.iterable)}>'

    @property
    def length(self):
        return len(self.iterable)

    @staticmethod
    def _from(array_like):
        return ChainedArray(list(array_like))

    @staticmethod
    def _is_chain_list(obj):
        return isinstance(obj, ChainedArray)

    def concat(self, array_like):
        is_chain_list = isinstance(array_like, ChainedArray)
        array = array_like.iterable if is_chain_list else list(array_like)
        return ChainedArray(self.iterable + array)

    def copy_within(self, target, start=0, end=None):
        if end is None:
            end = self.length
        if target >= self.length:
            return self
        copied_part = self.iterable[start:end]

        for copied_idx in range(len(copied_part)):
            iterable_idx = copied_idx + target
            self.iterable[iterable_idx] = copied_part[copied_idx]
        return self

    def entries(self):
        return iter(self.iterable)

    def every(self, callback):
        for item in self.iterable:
            if not callback(item):
                return False
        return True

    def fill(self, value, start=0, end=None):
        if start < 0:
            start = self.length + start
        if end is None:
            end = self.length
        elif end < 0:
            end = self.length + end
        array = self.iterable.copy()
        for idx in range(start, end):
            array[idx] = value
        return ChainedArray(array)

    def filter(self, callback):
        param_length = callback.__code__.co_argcount
        return ChainedArray([
            item
            for idx, item in enumerate(self.iterable)
            if callback_wrapper(callback, item, idx, self.iterable, param_length)
        ])

    def find(self, callback):
        param_length = callback.__code__.co_argcount
        for idx, item in enumerate(self.iterable):
            if callback_wrapper(
                    callback,
                    item,
                    idx,
                    self.iterable,
                    param_length):
                return item

    def find_index(self, callback):
        param_length = callback.__code__.co_argcount
        for idx, item in enumerate(self.iterable):
            if callback_wrapper(
                    callback,
                    item,
                    idx,
                    self.iterable,
                    param_length):
                return idx

    def flat(self, depth=1):
        array = self.iterable.copy()
        return ChainedArray(_flatten(array, depth))

    def flat_map(self, callback):
        array = self.map(callback)
        return ChainedArray(_flatten(array.iterable, 1))

    def for_each(self, callback):
        param_length = callback.__code__.co_argcount
        for idx, item in enumerate(self.iterable):
            callback_wrapper(callback, item, idx, self.iterable, param_length)

    def includes(self, value, from_index=0):
        if from_index >= self.length:
            return False
        return value in self.iterable[from_index:]

    def index_of(self, value, from_index=0):
        return self.iterable[from_index:].index(value)

    def join(self, separator=','):
        return separator.join(self.iterable)

    def keys(self):
        return iter(range(self.length))

    def last_index_of(self, value, from_index=None):
        if from_index is None:
            from_index = self.length - 1
        for idx, element in range(from_index, 0, -1):
            if value == element:
                return idx

    def map(self, callback):
        param_length = callback.__code__.co_argcount
        return ChainedArray([
            callback_wrapper(callback, item, idx, self.iterable, param_length)
            for idx, item in enumerate(self.iterable)
        ])

    def pop(self):
        return self.iterable.pop()

    def push(self, element):
        self.iterable.append(element)
        return self.length
