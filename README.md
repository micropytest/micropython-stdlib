# MicroPython Standard libraries from Python

Implementations of **Python** standard libraries for **MicroPython**.

## enum

Supported:

- ***`IntEnum`***

- ***`StrEnum`***

- ***`@unique`***

Due to **MicroPython** constraints, the enumeration classes must be decorated with **`@unique`**.
Example:

```python
from enum import IntEnum, unique

# class definition
@unique
class Color(IntEnum):
  RED = 1
  BLUE = 2
  GREEN = 3

# from value
red = Color(1)

# from name
red = Color.RED
```


## typing

Supported:

- ***`final`***

- ***`override`***
