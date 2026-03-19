__all__ = [
  "enum",
  "IntEnum",
  "StrEnum",
]


class _Enum:
  """Base for the enums.

  Attributes:
    _v2i: Value to enum instance map. Used by OurEnumType(value).
  """

  @classmethod
  def __init_subclass__(cls: type):
    # (1) init
    cls._v2i = {}

    # (2) get the target data type such as int (for IntEnum) or str (for StrEnum)
    Target = int if issubclass(cls, IntEnum) else str

    # (3) create the real enum instances defined by the user
    for name, value in list(cls.__dict__.items()):
      # pre: skip private members, methods and callables
      if name.startswith("_") or callable(value):
        continue

      # pre: value must be instance of Target
      if not isinstance(value, Target):
        raise TypeError(
          f"Enum literal value '{value}' ({type(value).__name__}) must be {Target.__name__}."
        )

      # create instance
      i = cls(value)
      i._name_ = name  # type: ignore

      # add instance to the class
      setattr(cls, name, i)
      cls._v2i[value] = i

    # (4) return enum class
    return cls


class IntEnum(int, _Enum):
  """An enumeration where all its values must be integers.

  Observations:
  - This must be defined with @enum too. Meta classes unsupported.
  - This can be accessed from something suc as, for example, OurEnumType.LITERAL.
  - @classmethod needed in __init_subclass__(), due to MicroPython.
  """


class StrEnum(str, _Enum):
  """An enumeration where all its values must be strings.

  Observations:
  - The IntEnum observations are applied to StrEnum.
  """


def enum(cls: type) -> type:
  """Generates the correct enumeration.

  Observations:
  - Needed due to __init_subclass__() is not automatically called by MicroPython.
  - It will be removed when MicroPython calls it.
  """

  # (1) adapt the literals
  cls.__init_subclass__()

  # (2) replace __new__ by factory function
  def new(cls, v: int | str) -> IntEnum | StrEnum:
    if i := cls._v2i.get(v):
      return i

    raise ValueError(f"Value '{v}' not found in {cls.__name__}.")

  setattr(cls, "__new__", new)

  # (3) return
  return cls
