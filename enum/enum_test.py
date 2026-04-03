import unittest
from enum import IntEnum, StrEnum, unique  # type: ignore


# The test int enum.
@unique
class IColor(IntEnum):
  RED = 1
  GREEN = 2
  BLUE = 3


# The test str enum.
@unique
class SColor(StrEnum):
  RED = "r"
  GREEN = "g"
  BLUE = "b"


class TestIntEnum(unittest.TestCase):
  def test_values(self) -> None:
    """Check that an IntEnum subclass is well-defined."""

    self.assertIsInstance(c := IColor.BLUE, IColor)
    self.assertIsInstance(c, int)
    self.assertEqual(c, 3)
    self.assertEqual(c.name, "BLUE")
    self.assertEqual(c.value, 3)

  def test_call_returns_i(self) -> None:
    """Check that Color(value) returns a Color instance if value found."""

    self.assertIs(IColor(1), IColor.RED)
    self.assertIs(IColor(2), IColor.GREEN)
    self.assertIs(IColor(3), IColor.BLUE)

  def test_call_raises_error(self) -> None:
    """Check that Color(value) raises error if value not found."""

    # (1) act
    with self.assertRaises(ValueError) as out:
      IColor(123)

    # (2) assessment
    self.assertEqual(str(out.exception), "Value '123' not found in IColor.")

  def test_invalid_enum_value_due_to_type(self) -> None:
    """Check that enum definition raises error if value is not int."""

    # (1) act
    with self.assertRaises(ValueError) as out:

      @unique
      class IColor(IntEnum):
        RED = 1
        GREEN = "2"  # type: ignore
        BLUE = 3

    # (2) assessment
    self.assertEqual(str(out.exception), "Enum literal value '2' (str) must be int.")

  def test_invalid_enum_value_due_to_duplicate(self) -> None:
    """Check that enum definition raises error if value is a duplicate."""

    # (1) act
    with self.assertRaises(ValueError) as out:

      @unique
      class IColor(IntEnum):
        RED = 1
        GREEN = 2
        BLUE = 1

    # (2) assessment
    self.assertEqual(str(out.exception), "duplicate values found in <enum 'IColor'>: RED -> BLUE")


class TestStrEnum(unittest.TestCase):
  def test_values(self) -> None:
    """Check that a StrEnum subclass is well-defined."""

    self.assertIsInstance(c := SColor.BLUE, SColor)
    self.assertIsInstance(c, str)
    self.assertEqual(c, "b")
    self.assertEqual(c.name, "BLUE")  # type: ignore
    self.assertEqual(c.value, "b")  # type: ignore

  def test_call_returns_i(self) -> None:
    """Check that Color(value) returns a Color instance if value found."""

    self.assertIs(SColor("r"), SColor.RED)
    self.assertIs(SColor("g"), SColor.GREEN)
    self.assertIs(SColor("b"), SColor.BLUE)

  def test_call_raises_error(self) -> None:
    """Check that Color(value) raises error if value not found."""

    # (1) act
    with self.assertRaises(ValueError) as out:
      SColor("rgb")

    # (2) assessment
    self.assertEqual(str(out.exception), "Value 'rgb' not found in SColor.")
