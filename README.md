# MicroPython Standard libraries from Python

Implementations of **Python** standard libraries for **MicroPython**.

## enum

Due to **MicroPython** constraints, the enumeration must be decorated with **`@enum`**.
When **MicroPython** enhanced, this decorator will be removed.
Example:

```python
from enum import IntEnum, enum

# class definition
@enum
class Color(IntEnum):
  RED = 1
  BLUE = 2
  GREEN = 3

# from value
red = Color(1)

# from name
red = Color.RED
```
