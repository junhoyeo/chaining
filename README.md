# ⛓ Pychaining
> Functional chaining in Python

```python
from chaining import ChainList

array = ChainList([1, 2, 3])
print(array)
# <ChainList [1, 2, 3]>
print(array.length) # property length
# 3

other_array = ChainList._from('chain') # static method from
print(other_array)
# <ChainList ['c', 'h', 'a', 'i', 'n']>
print(other_array.length)
# 5

multiply = lambda item: item * 2

print(array.map(multiply)) # instance method map
# [2, 4, 6]

print(array.concat(other_array)) # instance method concat
# [1, 2, 3, 'c', 'h', 'a', 'i', 'n']
```
