# ⛓ Chaining
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/chaining)](https://pypi.org/project/chaining/)
[![MIT LICENSE](https://img.shields.io/pypi/l/chaining)](https://github.com/junhoyeo/chaining/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/chaining.svg)](https://badge.fury.io/py/chaining)
[![PyPI monthly downloads](https://img.shields.io/pypi/dm/chaining)](https://pypistats.org/packages/chaining)

> Package that implements functional chaining in Python, which behaves like JavaScript

## 📦 Installation
This package is not ready to be used in production; There are lots of things still left to be implemented and optimized!

```bash
# only python 3.6 or newer
pip3 install chaining
```

## 🔥 Action

### ChainList
```python
>>> from chaining import ChainList
>>> array = ChainList([1, 2, 3])
>>> array.length
3
>>> array.map(lambda item: item * 2)
<ChainList [2, 4, 6]>
>>> other_array = ChainList._from('chain').map(lambda item, idx: ord(item) + idx)
>>> other_array.iterable
[99, 105, 99, 108, 114]
>>> array.concat(other_array)
<ChainList [1, 2, 3, 99, 105, 99, 108, 114]>
```
