import unittest
from enum import (
  IntEnum,
  StrEnum,  # type: ignore
  enum,  # type: ignore
)


# The test int enum.
@enum
class IColor(IntEnum):
  RED = 1
  GREEN = 2
  BLUE = 3


# The test str enum.
@enum
class SColor(StrEnum):
  RED = "r"
  GREEN = "g"
  BLUE = "b"


class TestIntEnum(unittest.TestCase):
  def test_values(self) -> None:
    """Check that an IntEnum subclass is well-defined."""

    assert IColor.BLUE == 3
    assert isinstance(IColor.BLUE, int)
    assert isinstance(IColor.BLUE, IColor)

  def test_call_returns_i(self) -> None:
    """Check that Color(value) returns a Color instance if value found."""

    assert IColor(1) is IColor.RED
    assert IColor(2) is IColor.GREEN
    assert IColor(3) is IColor.BLUE

  def test_call_raises_error(self) -> None:
    """Check that Color(value) raises error if value not found."""

    # (1) act
    with self.assertRaises(ValueError) as out:
      IColor(123)

    # (2) assessment
    assert str(out.exception) == "Value '123' not found in IColor."

  def test_invalid_enum_value(self) -> None:
    """Check that enum definition raises error if value is not int."""

    # (1) act
    with self.assertRaises(TypeError) as out:

      @enum
      class IColor(IntEnum):
        RED = 1
        GREEN = "2"  # type: ignore
        BLUE = 3

    # (2) assessment
    assert str(out.exception) == "Enum literal value '2' (str) must be int."


class TestStrEnum(unittest.TestCase):
  def test_values(self) -> None:
    """Check that a StrEnum subclass is well-defined."""

    assert SColor.BLUE == "b"
    assert isinstance(SColor.BLUE, str)
    assert isinstance(SColor.BLUE, SColor)

  def test_call_returns_i(self) -> None:
    """Check that Color(value) returns a Color instance if value found."""

    assert SColor("r") is SColor.RED
    assert SColor("g") is SColor.GREEN
    assert SColor("b") is SColor.BLUE

  def test_call_raises_error(self) -> None:
    """Check that Color(value) raises error if value not found."""

    # (1) act
    with self.assertRaises(ValueError) as out:
      SColor("rgb")

    # (2) assessment
    assert str(out.exception) == "Value 'rgb' not found in SColor."
