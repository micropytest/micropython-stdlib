__all__ = [
  "unique",
  "IntEnum",
  "StrEnum",
]


class _Enum:
  """Base for the enums.

  Attributes:
    _v2i: Value to enum instance map. Used by OurEnumType(value).
  """

  _Target = None
  """Data type for the values."""

  @property
  def name(self) -> str:
    return self._name_  # type: ignore

  @classmethod
  def __init_subclass__(cls: type):
    # (1) init
    cls._v2i = {}

    # (2) get the target data type such as int (for IntEnum) or str (for StrEnum)
    Target = cls._Target

    # (3) create the real enum instances defined by the user
    for name, value in list(cls.__dict__.items()):
      # pre: skip private members, methods and callables
      if name.startswith("_") or callable(value):
        continue

      # pre: value must be instance of Target
      if not isinstance(value, Target):
        raise ValueError(
          f"Enum literal value '{value}' ({type(value).__name__}) must be {Target.__name__}."
        )

      # pre: value must already be in use
      if (i := cls._v2i.get(value)) is not None:
        raise ValueError(f"duplicate values found in <enum '{cls.__name__}'>: {i.name} -> {name}")

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

  _Target = int

  @property
  def value(self) -> int:
    return self


class StrEnum(str, _Enum):
  """An enumeration where all its values must be strings.

  Observations:
  - The IntEnum observations are applied to StrEnum.
  """

  _Target = str

  @property
  def value(self) -> str:
    return self


def unique(cls: type) -> type:
  """Sets that the enumeration can't have duplicated values.

  Observations:
  - Needed due to __init_subclass__() is not automatically called by MicroPython.
  - This constraint will be removed when MicroPython calls it, allowing to define
    an enumeration without this decorator.
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
