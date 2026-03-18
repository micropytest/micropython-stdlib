__all__ = [
  "IntEnum",
  "enum",
]


class IntEnum(int):
  """An enumeration where all its values must be integers.

  Observations:
  - This must be defined with @enum too. Meta classes unsupported.
  - This can be accessed from EnumType.LITERAL.
  - @classmethod needed in __init_subclass__(), only in MicroPython.

  Attributes:
    _v2i: Value to enum instance map. Used by EnumType(value).
  """

  @classmethod
  def __init_subclass__(cls: type):
    # (1) init
    cls._v2i = {}

    # (2) adapt its enum instances created by MicroPython
    # create the real enum instances
    for name, value in list(cls.__dict__.items()):
      # pre: skip private members, methods and callables
      if name.startswith("_") or callable(value):
        continue

      # create instance
      i = cls(value)
      i._name_ = name

      # add instance to the class
      setattr(cls, name, i)
      cls._v2i[value] = i

    # (3) return enum class
    return cls


def enum(cls: type) -> type:
  """Generates the correct enumeration.

  Observations:
  - Needed due to __init_subclass__() is not automatically called.
  """

  # (1) adapt the literals
  cls.__init_subclass__()

  # (2) replace __new__ for allowing EnumType(value)
  def new(cls, v: int) -> IntEnum:
    if i := cls._v2i.get(v):
      return i

    raise ValueError(f"Value '{v}' not found in {cls.__name__}(IntEnum).")

  setattr(cls, "__new__", new)

  # (3) return
  return cls
